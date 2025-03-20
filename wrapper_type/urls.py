from django.urls import path
from .views import wrapperView

urlpatterns = [
    path('add/', wrapperView.as_view(), name='create_breads_size'),
    path('all/', wrapperView.as_view(), name='view_category'),
]
