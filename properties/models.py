from django.db import models
from django.utils.text import slugify
import random
from agents.models import Agent

CATEGORY_CHOICE =(
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
    ('Short Let', 'Short Let'),
)
class Category(models.Model):
    title = models.CharField(max_length=100,choices=CATEGORY_CHOICE)
    def __str__(self):
        return self.title


STATUS_CHOICE =(
    ('Sold', 'Sold'),
    ('Rented', 'Rented'),
    ('Available', 'Available'),
)
LISTING_TYPE =(
    ('House', 'House'),
    ('Land', 'Land'),
)
FURNISHING_TYPE  =(
    ('Furnished', 'Furnished'),
    ('Semi-Furnished', 'Semi-Funished'),
    ('Not Furnished', 'Not Furnished'),
)
class Listing(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    listing_id = models.IntegerField(unique=True,blank=True, null=True)
    listing_type = models.CharField(max_length=150,choices=LISTING_TYPE)
    title = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price =models.IntegerField()
    bedrooms =models.IntegerField(blank=True, null=True)
    bathrooms =models.IntegerField(blank=True, null=True)
    toilets =models.IntegerField(blank=True, null=True)
    garage =models.IntegerField(blank=True, null=True)
    sqft =models.IntegerField(blank=True, null=True)
    lot_size =models.FloatField(blank=True, null=True)
    status =models.CharField(max_length=150,choices=STATUS_CHOICE)
    furnish =models.CharField(max_length=150,choices=FURNISHING_TYPE,blank=True, null=True)
    photo_main = models.ImageField(upload_to='listing/%Y%m%d/')
    photo_1 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_2 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_3 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_4 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_5 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_6 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_7 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_8 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    photo_9 = models.ImageField(upload_to='listing/%Y%m%d/',blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,)
    updated_at = models.DateTimeField(auto_now=True,blank=True,)

    def save(self, *args, **kwargs):
        # Generate a new random 4-digit number for listing_id
        if not self.listing_id:
            self.listing_id = random.randint(1000, 9999)
            while Listing.objects.filter(listing_id=self.listing_id).exists():
                # Ensure uniqueness by regenerating if the chosen number already exists
                self.listing_id = random.randint(1000, 9999)
        # Generate slug when saving the object
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - Id {self.listing_id}'



class Inquiry(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.CharField(max_length = 1000,blank=True,null=True)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(auto_now_add=True,blank=True,)
  user_id = models.IntegerField(blank=True)

  def __str__(self):
    return self.name