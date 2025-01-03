import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

  

class Profile(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=500,null=True, blank=True)
    username = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    short_intro = models.CharField(max_length=200,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    social_github = models.CharField(max_length=200,null=True, blank=True)
    social_twitter = models.CharField(max_length=200,null=True, blank=True)
    social_linkedin = models.CharField(max_length=200,null=True, blank=True)
    social_website = models.CharField(max_length=200,null=True, blank=True)
    social_youtube = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return str(self.user.username)
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField( max_length=254, null=True, blank=True)
    subject = models.CharField(max_length=200, )
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False) 

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created']


