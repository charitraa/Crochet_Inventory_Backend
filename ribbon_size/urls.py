from django.urls import path
from .views import RibbonView

urlpatterns = [
    path('add/', RibbonView.as_view(), name='create_breads_size'),  # Endpoint for creating a new category (POST request)
    path('all/', RibbonView.as_view(), name='view_category'),
    
]
