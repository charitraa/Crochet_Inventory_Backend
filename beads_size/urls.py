from django.urls import path
from .views import BeadsView, BreadDeleteView

urlpatterns = [
    path('add/', BeadsView.as_view(), name='create_breads_size'),  # Endpoint for creating a new category (POST request)
    path('all/', BeadsView.as_view(), name='view_category'),
    path('delete/<str:pk>/', BreadDeleteView.as_view(), name='view_category'),  # Endpoint for retrieving all categories (GET request)
        # Endpoint for retrieving all categories (GET request)
    
]
