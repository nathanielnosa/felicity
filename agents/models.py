from django.db import models

# Create your models here.
class Agent(models.Model):
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

    def __str__(self):
        return self.name
