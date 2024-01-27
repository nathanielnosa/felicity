from django.shortcuts import render,redirect

from . models import Agent
from . forms import UserProfile,Editprofile

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    agents = Agent.objects.all().order_by('-hired_at')
    context={
        'agents':agents
    }
    return render(request, 'agents/agents.html',context)


def signup(request):
    return render(request, 'agents/signup.html')

# login
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    page = 'login'
    if request.method == 'POST':
        username =  request.POST['username'].lower()
        password =  request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Username does not exit.')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'dashboard')
        else:
            messages.error(request, 'Username or Password does not match.')

    return render(request, 'agents/registerlogin.html')

# logout user
def logoutuser(request):
    logout(request)
    messages.success(request, 'User logged out.')
    return redirect('login')


# registration
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

     
    page = 'register'
    forms = UserProfile()
    if request.method == 'POST':
        user_reg = request.POST.get('is_user')
        agent_reg = request.POST.get('is_agent')

        if user_reg == 'true':   
            forms = UserProfile(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data.get('username')
                email = forms.cleaned_data.get('email')
                password = forms.cleaned_data.get('password1')
                password2 = forms.cleaned_data.get('password2')

                if password != password2:
                    messages.error(request, "Password not match")
                    return redirect('register')
            
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                user = User.objects.create_user(username,email,password)
                forms = forms.save(commit=False)
                forms.user = user
                forms.save()

                subject = 'Welcome To Felicity Property Limited'
                body = f'Greetings from Felicity Property Limited. \n Thank you for signing up for FelicityProperty Support. You now have access to Felicity Property platforms. \n If you interact with Felicity Property Limited, you must provide your full information after signup to verify \nwho you are and whether you have permission to access the resources you are requesting.\n Welcome to the Felicity Property Services community!\n —The Felicity Services Team'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently= False
                    )
                messages.success(request, "User Registration successful")
                login(request, user)
                return redirect('editprofile')
            else:
                messages.error(request, 'User Registration Failed.')

        elif agent_reg == 'true':
            forms = UserProfile(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data.get('username')
                email = forms.cleaned_data.get('email')
                password = forms.cleaned_data.get('password1')
                password2 = forms.cleaned_data.get('password2')

                if password != password2:
                    messages.error(request, "Password not match")
                    return redirect('register')
            
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                user = User.objects.create_user(username,email,password)


                forms = forms.save(commit=False)
                forms.user = user
                forms.save()

                subject = 'Welcome To Felicity Property Limited'
                body = f'Greetings from Felicity Property Limited. \n Thank you for signing up for FelicityProperty Support. You now have access to Felicity Property platforms. \n If you interact with Felicity Property Limited, you must provide your full information after signup to verify \n who you are and whether you have permission to access the resources you are requesting.\n Welcome to the Felicity Property Services community!\n —The Felicity Services Team'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently= False
                    )
                messages.success(request, "Agent Registration successful")
                login(request, user)
                return redirect('editprofile')
            else:
                messages.error(request, 'Agent Registration Failed.')

        else:
            return redirect('signup')

    context={
        'forms':forms,
        'page':page
    }
    return render(request, 'agents/registerlogin.html',context)


# user account page
@login_required(login_url="login")
def dashboard(request):
  profile = request.user.agent
  listings = profile.listing_set.all()

  context = {
    'profile':profile,
    'project':listings

  }

  return render(request, 'agents/dashboard.html', context)

# edit user profile
@login_required(login_url="login")
def editprofile(request):
  profile = request.user.agent
  form = Editprofile(instance=profile)
  if request.method == 'POST':
    form = Editprofile(request.POST, request.FILES, instance = profile)
    if form.is_valid():
      form.save()

      return redirect('dashboard')
  context={
    'form':form
  }
  return render(request, 'agents/editprofile.html', context)