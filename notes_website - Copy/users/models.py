from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    sem_choices=((1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five'),(6,'Six'),(7,'Seven'),(8,'Eight'))
    branch_choices=(
      ('comps', 'Computer Science'),
      ('it', 'Information Technology'),
      ('extc','Electronics and Telecom'),
      ('etrx','Electronics')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #first_name=models.CharField(max_length=100)
    #last_name=models.CharField(max_length=100)
    sem=models.IntegerField(choices=sem_choices,null=True)
    branch=models.CharField(max_length=100,choices=branch_choices)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
