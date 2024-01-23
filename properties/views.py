from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from . models import *
# Create your views here.

def index(request):
    listings = Listing.objects.all().order_by('-created_at')
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context={
        'listings':paged_listings
    }
    return render(request, 'properties/listings.html',context)

def listing(request,slug):
    listing = get_object_or_404(Listing, slug=slug)
    context={
        'shows':listing
    }
    return render(request, 'properties/listing.html',context)

# def search(request):
#     return render(request, 'properties/agents.html')
