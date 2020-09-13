from django import forms
from .models import Note, Subject
from users.models import UserProfile
from notes.views import *
class CreateNoteForm(forms.ModelForm):
    class Meta:
        model=Note 
        fields=['name','description','subjectname','filename']

class FilteringFormOne(forms.Form):
    sem_choices=((0,'All'),(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five'),(6,'Six'),(7,'Seven'),(8,'Eight'))
    branch_choices=(
      ('All','All branches'),
      ('comps', 'Computer Science'),
      ('it', 'Information Technology'),
      ('extc','Electronics and Telecom'),
      ('etrx','Electronics')
    )
    branch=forms.ChoiceField(choices=branch_choices,required=False)
    sem=forms.ChoiceField(choices=sem_choices,required=False)
    #print(fsem)

class FilteringFormTwo(forms.Form):
    branch_choices=(
      ('All','All branches'),
      ('comps', 'Computer Science'),
      ('it', 'Information Technology'),
      ('extc','Electronics and Telecom'),
      ('etrx','Electronics')
    )
    branch=forms.ChoiceField(choices=branch_choices,required=False)

#class FilteringFormThree(forms.Form):
    #field1 = forms.ModelChoiceField(queryset = MyModel.objects.all() )
