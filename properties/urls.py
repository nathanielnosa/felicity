from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='property'),
    path('<slug:slug>/', views.listing, name='listing'),
    # path('search/', views.search, name='search'),
]
