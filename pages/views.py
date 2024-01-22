from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')
def property(request):
    return render(request, 'pages/property.html')
def agent(request):
    return render(request, 'pages/agents.html')
def contact(request):
    return render(request, 'pages/contact.html')