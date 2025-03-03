from django.urls import path
from .views import SizeView

urlpatterns = [
    path('add/', SizeView.as_view(), name='create_size_type'),  # Endpoint for creating a new colors (POST request)
    path('all/', SizeView.as_view(), name='view_size_type'),  # Endpoint for retrieving all colors (GET request)
    
    
]
