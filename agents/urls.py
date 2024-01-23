from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='agent'),
    path('<str:id>/', views.agent, name='agent'),
]
