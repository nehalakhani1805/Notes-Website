from django.shortcuts import render,redirect 
from .forms import RegistrationForm,ProfileUpdateForm, UpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if(request.method=="POST"):
		form=RegistrationForm(request.POST)
		#p_form=ProfileForm(request.POST)
		#p_form.instance.user=request.user
		if form.is_valid() :#and p_form.is_valid():
			form.save()
			#p_form.save()
			messages.success(request, f'Welcome')
			return redirect('home')
	else:
		form=RegistrationForm()
		#p_form=ProfileForm()
	return render(request,'users/register.html', {'form':form})#,'p_form':p_form})
@login_required
def profile(request):
	if(request.method=="POST"):
		form=UpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,instance=request.user.userprofile)
		#p_form.instance.user=request.user
		if form.is_valid() and p_form.is_valid():
			form.save()
			p_form.save()
			messages.success(request, f'Welcome')
			return redirect('home')
	else:
		form=UpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.userprofile)
	return render(request,'users/profile.html', {'form':form,'p_form':p_form})