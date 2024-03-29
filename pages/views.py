from django.shortcuts import render,redirect
from django.db.models import Q
from properties.models import *
from properties.choices import *
from agents.models import *
from . models import ContactUs

from django.core.mail import send_mail
from django.conf import settings


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

def search(request):
    queryset = Listing.objects.order_by('-created_at')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords) | Q(address__icontains=keywords) | Q(price__icontains=keywords) | Q(category__title__iexact=keywords))
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)
    # bedrooms
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        if bedroom:
            queryset = queryset.filter(bedrooms__lte=bedroom)
    
    # bathroom
    if 'bathroom' in request.GET:
        bathroom = request.GET['bathroom']
        if bathroom:
            queryset = queryset.filter(bathrooms__lte=bathroom)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)
    # garage
    if 'garage' in request.GET:
        garage = request.GET['garage']
        if garage:
            queryset = queryset.filter(garage__lte=garage)
    # type
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset = queryset.filter(category__title__icontains=type)
    

    context ={
        'listings': queryset,
        'values':request.GET
    }
    return render(request, 'pages/search.html',context)
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        datas = ContactUs(name=name,email=email,subject=subject,message=message)

        datas.save()
        body=message
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently= False
            )
        return redirect('contact')



    return render(request, 'pages/contact.html')

