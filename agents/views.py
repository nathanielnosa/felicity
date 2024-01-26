from django.shortcuts import render
from django.contrib import messages

# messages.add_message(request, messages.INFO, "Hello world.")
# Create your views here.
def index(request):
    return render(request, 'agents/agents.html')
def agent(request):
    return render(request, 'agents/agent.html')
