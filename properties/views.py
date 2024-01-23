from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'properties/listings.html')
def listing(request):
    return render(request, 'properties/listing.html')

# def search(request):
#     return render(request, 'properties/agents.html')
