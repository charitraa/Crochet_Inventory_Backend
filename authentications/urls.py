
from django.contrib import admin
from django.urls import include, path
from .views import LoginView, CreateUserView,GetUserDataView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('me/', GetUserDataView.as_view(), name='me'),



    
]
