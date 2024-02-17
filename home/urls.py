from .views import BlogView
from django.urls import path

urlpatterns = [
    path('home/', BlogView.as_view(), name='blog'),
    
]