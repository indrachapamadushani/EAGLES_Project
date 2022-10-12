from django.db import models
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime


# Create your models here.
# Defining an user profile 
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
 
# Class for Uploading Posts#
class Posts(models.Model):
    id = models.UUIDFIELD(primary_key= True, default =uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    no_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.use
    
    
    

