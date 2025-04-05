from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings, name='listings'),

    # Optional fix:
    path('', views.index),  # Add this only if you have views.index
]
