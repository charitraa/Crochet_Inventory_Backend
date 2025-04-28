# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('forgot/', views.forgot_password, name='forgot-password'),
    path('reset/', views.reset_password, name='reset-password'),
]
