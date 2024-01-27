from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from . models import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateListing
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



@login_required(login_url="login")
def createlisting(request):
  profile = request.user.agent
  form = CreateListing()

  if request.method == 'POST':
    form = CreateListing(request.POST, request.FILES)
    if form.is_valid:
      listing = form.save(commit=False)
      listing.agent = profile
      listing.save()
      messages.success(request, 'Listing Added Successfully.')


      return redirect('dashboard')
  context = {
    'form':form,
  }
  return render(request, 'properties/create.html',context)


@login_required(login_url="login")
def updatelisting(request, id):
  profile = request.user.agent
  update =  profile.listing_set.get(pk=id)
  form = CreateListing(instance= update)

  if request.method == 'POST':
    form = CreateListing(request.POST, request.FILES, instance=update)
    if form.is_valid:
      form.save()
      messages.success(request, 'Listing Update Successfully.')

  
      return redirect('dashboard')
  context = {
    'form':form,
  }
  return render(request, 'properties/create.html',context)

@login_required(login_url="login")
def deletelisting(request, id):
  profile = request.user.agent
  delete = profile.listing_set.get(pk=id)
  if request.method == "POST":
    delete.delete()
    messages.success(request, 'user delete listing successfully.')

    return redirect('property')

  context = {
    'delete':delete
  }
  return render(request, '_partials/_delete.html',context)
