from django.db import models

# Create your models here.


# contact form
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class Testimony(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    photo_main = models.ImageField(upload_to='testimony/%Y%m%d/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name

CATEGORY_CHOICE =(
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
    ('Short Let', 'Short Let'),
)    
class Slider(models.Model):
    address = models.CharField(max_length=255)
    title = models.TextField(blank=True,null=True)
    amount = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICE)
    photo_main = models.ImageField(upload_to='testimony/%Y%m%d/',blank=True,null=True)

    def __str__(self):
        return self.address

    
