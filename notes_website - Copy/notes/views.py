from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateNoteForm,FilteringFormOne, FilteringFormTwo
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponse
# Create your views here.
fsem='0'
fbranch='All'
def home(request):
    notes=Note.objects.all().order_by('-date_posted')
    form=FilteringFormOne()
    form2=FilteringFormTwo()
    if request.method=='POST':
        form=FilteringFormOne(request.POST)
        #form=FilteringFormTwo(request.POST)
        #form.instance.author=request.user
        if form.is_valid() :
            #form.save()
            #return redirect('home')
            fsem=form.cleaned_data['sem']
            fbranch=form.cleaned_data['branch']
            #print(form2.cleaned_data['branch'])
            if form.cleaned_data['sem']=='0' and form.cleaned_data['branch']=='All':
                print("hey")
                notes=Note.objects.all().order_by('-date_posted')
                #return redirect ('home')
            else:
                if form.cleaned_data['sem']==0:
                    notes=Note.objects.filter(subjectname__branch=form.cleaned_data['branch']).all()
                    #return redirect ('home')
                elif form.cleaned_data['branch']=='All':
                    notes=Note.objects.filter(subjectname__sem=form.cleaned_data['sem']).all()
                    #return redirect ('home')
                else:
                    notes=Note.objects.filter(subjectname__sem=form.cleaned_data['sem'],subjectname__branch=form.cleaned_data['branch']).all()
                    #return redirect ('home')

    #else:
        #form=FilteringForm()
    return render(request,'notes/home.html',{'title':'Home Page','notes':notes,'form':form})
def about(request):
    return render(request,'notes/about.html',{'title':'About Page'})
@login_required
def create(request):
    if request.method=='POST':
        form=CreateNoteForm(request.POST,request.FILES)
        form.instance.author=request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CreateNoteForm()
    return render(request,'notes/create.html',{'form':form})

@login_required
def mynotes(request):
    notes=Note.objects.filter(author=request.user).order_by('-date_posted')
    return render(request,'notes/home.html',{'title':'Home Page','notes':notes})