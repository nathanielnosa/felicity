from django.shortcuts import render
from properties.models import *
# Create your views here.
def index(request):
    listing = Listing.objects.all()[:4]

    context={
        'listing': listing
    }
    return render(request, 'pages/index.html',context)
def about(request):
    return render(request, 'pages/about.html')
def contact(request):
    return render(request, 'pages/contact.html')