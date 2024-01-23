from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'agents/agents.html')
def agent(request):
    return render(request, 'agents/agent.html')
