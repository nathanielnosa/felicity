from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='agent'),
    path('<int:id>/', views.singleagent, name='singleagent'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('logout', views.logoutuser, name='logout'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('editprofile', views.editprofile, name='editprofile'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:id>/', views.viewmesg, name='message'),
    path('sendmessage/<str:pk>/', views.sendmessage, name='sendmessage'),
]
