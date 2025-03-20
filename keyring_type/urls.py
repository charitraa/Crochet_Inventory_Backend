from django.urls import path
from .views import KeyringView

urlpatterns = [
    path('add/', KeyringView.as_view(), name='create_breads_size'),
    path('all/', KeyringView.as_view(), name='view_category'),
]
