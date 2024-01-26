from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length=100)
    description = models.TextField( blank=True,null=True)
    phone = models.CharField(max_length=12, blank=True,null=True)
    mobile = models.CharField(max_length=12, blank=True,null=True)
    email = models.EmailField()
    facebook = models.CharField(max_length=225, blank=True,null=True)
    instagram = models.CharField(max_length=225, blank=True,null=True)
    twitter = models.CharField(max_length=225, blank=True,null=True)
    linkedin = models.CharField(max_length=225, blank=True,null=True)
    photo_main = models.ImageField(upload_to='agent/%Y%m%d/')
    hired_at = models.DateTimeField(auto_now_add=True,blank=True,)
    updated_at = models.DateTimeField(auto_now=True,blank=True,)
    is_mvp = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(Agent, on_delete=models.SET_NULL, null= True, blank=True)
    recipient = models.ForeignKey(Agent, on_delete=models.SET_NULL, null= True, blank=True, related_name='messages')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    is_read = models.BooleanField(default=False, null= True)
    subject=models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self):
        return self.subject
