from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='property'),
    path('<slug:slug>/', views.listing, name='listing'),
    path('category/<str:id>/', views.category, name='category'),

    path('createlisting', views.createlisting, name='createlisting'),
    path('updatelisting/<str:id>/', views.updatelisting, name='updatelisting'),
    path('deletelisting/<str:id>/', views.deletelisting, name='deletelisting'),

]
