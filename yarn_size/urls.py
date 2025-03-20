from django.urls import path
from .views import YarnView

urlpatterns = [
    path('add/', YarnView.as_view(), name='create_breads_size'),  # Endpoint for creating a new category (POST request)
    path('all/', YarnView.as_view(), name='view_category'),
    
]
