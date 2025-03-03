from django.urls import path
from .views import CategoryView, CategoryViewById

urlpatterns = [
    path('add/', CategoryView.as_view(), name='create_category'),  # Endpoint for creating a new category (POST request)
    path('all/', CategoryView.as_view(), name='view_category'),  # Endpoint for retrieving all categories (GET request)
    path('get/<str:pk>/', CategoryViewById.as_view(), name='get_category'),  # Endpoint for fetching a specific category by ID (GET request)
    path('edit/<str:pk>/', CategoryViewById.as_view(), name='edit_category'),  # Endpoint for updating a category by ID (PUT request)
    path('delete/<str:pk>/', CategoryViewById.as_view(), name='delete_category'),  # Endpoint for deleting a category by ID (DELETE request)
]
