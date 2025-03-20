from django.urls import path
from .views import BeadsView

urlpatterns = [
    path('add/', BeadsView.as_view(), name='create_breads_size'),
    path('all/', BeadsView.as_view(), name='view_category'),
]
