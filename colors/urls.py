from django.urls import path
from .views import ColorView

urlpatterns = [
    path('add/', ColorView.as_view(), name='create_category'),  # Endpoint for creating a new colors (POST request)
    path('all/', ColorView.as_view(), name='view_category'),  # Endpoint for retrieving all colors (GET request)
    
]
