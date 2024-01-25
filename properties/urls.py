from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='property'),
    path('<slug:slug>/', views.listing, name='listing'),
    path('category/<str:id>/', views.category, name='category')
]
