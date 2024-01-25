from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from . models import *
# Create your views here.

def index(request):
    listings = Listing.objects.all().order_by('-created_at').filter(is_published=True)
    paginator = Paginator(listings,6)
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

def category(request,id):
    category = Listing.objects.all().filter(category=id)
    # Get the furnish choice from the query parameters (defaults to 'all' if not provided)
    furnish_choice = request.GET.get('furnish', 'all')

    # Filter listings based on the furnish choice
    if furnish_choice != 'all':
        category_listings = category.filter(furnish=furnish_choice)
    else:
        category_listings = Listing.objects.all().filter(category=id)


    context={
        'listings': category,
        'furnish_choice': furnish_choice,
        'category_id':id
    }
    return render(request, 'properties/category.html',context)
