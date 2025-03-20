from django.urls import path
from .views import WireView, WireSizeDeleteView

urlpatterns = [
    path('add/', WireView.as_view(), name='create_breads_size'),  # Endpoint for creating a new category (POST request)
    path('all/', WireView.as_view(), name='view_category'),
    path('delete/<str:pk>/', WireSizeDeleteView.as_view(), name='view_category'),

    
]
