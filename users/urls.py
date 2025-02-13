"""
URL configuration for crochet_inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import UserDetails, UserCreate, UserMeView
urlpatterns = [
    path('create/', UserCreate.as_view(), name='add_user'),
    path('get/<str:pk>/', UserDetails.as_view(), name='get_user'),
    path('update/<str:pk>/', UserDetails.as_view(), name='update_user'),
    path('delete/<str:pk>/', UserDetails.as_view(), name='delete_user'),
    path('me/', UserMeView.as_view(), name='user_detail'),



]
