from django.urls import path
from .views import ProductView, ProductViewById

urlpatterns = [
    # Endpoint to add a new product
    path('add/', ProductView.as_view(), name='add_product'),
    
    # Endpoint to get a product by its ID (Primary Key)
    path('get/<str:pk>/', ProductViewById.as_view(), name='get_product'),
    
    # Endpoint to edit/update a product by its ID
    path('edit/<str:pk>/', ProductViewById.as_view(), name='edit_product'),
    
    # Endpoint to delete a product by its ID
    path('delete/<str:pk>/', ProductViewById.as_view(), name='delete_product'),
    
    # Endpoint to get all products
    path('all/', ProductView.as_view(), name='view_product'),
]
