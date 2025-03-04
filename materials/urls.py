from django.urls import path
from .views import MaterialView, MaterialViewById

urlpatterns = [
    path('add/', MaterialView.as_view(), name='create_Material'),  # Endpoint for creating a new Material (POST request)
    path('all/', MaterialView.as_view(), name='view_Material'),  # Endpoint for retrieving all categories (GET request)
    path('get/<str:pk>/', MaterialViewById.as_view(), name='get_Material'),  # Endpoint for fetching a specific Material by ID (GET request)
    path('edit/<str:pk>/', MaterialViewById.as_view(), name='edit_Material'),  # Endpoint for updating a Material by ID (PUT request)
    path('delete/<str:pk>/', MaterialViewById.as_view(), name='delete_Material'),  # Endpoint for deleting a Material by ID (DELETE request)
]
