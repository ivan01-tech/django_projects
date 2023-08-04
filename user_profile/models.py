from django.contrib.auth.models import User
from django.db import models
import django.views.decorators.csrf

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE,to=User)
    city = models.CharField(blank=True,null=True,default="",max_length=50)
    phone_number = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.user.username