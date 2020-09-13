from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    sem_choices=((1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five'),(6,'Six'),(7,'Seven'),(8,'Eight'))
    branch_choices=(
      ('comps', 'Computer Science'),
      ('it', 'Information Technology'),
      ('extc','Electronics and Telecom'),
      ('etrx','Electronics')
    )
    #name=models.IntegerField(choices=sem_choices)
    name=models.CharField(max_length=100)
    sem=models.IntegerField(choices=sem_choices)
    branch=models.CharField(max_length=100,choices=branch_choices)
    #semname=models.ForeignKey('Semester',on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
class Note(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    subjectname=models.ForeignKey('Subject',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    filename=models.FileField(upload_to='notes/pdf/')
    def __str__(self):
        return self.name