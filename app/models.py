from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#user class is already their in authentication.so,
#we only import the path.import path is "from django.contrib.auth.models import User"


class Profile(models.Model):
    Username=models.OneToOneField(User,on_delete=models.CASCADE)
    Address=models.TextField()
    Profile_pic=models.ImageField()
