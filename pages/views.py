from django.shortcuts import render
from properties.models import *
from agents.models import *
# Create your views here.
def index(request):
    listing = Listing.objects.all().order_by('-created_at').filter(is_published=True)[:4]

    context={
        'listing': listing
    }
    return render(request, 'pages/index.html',context)
def about(request):
    agents = Agent.objects.all().order_by('-hired_at')
    context={
            'agents': agents
        }
    return render(request, 'pages/about.html',context)

def contact(request):
    return render(request, 'pages/contact.html')