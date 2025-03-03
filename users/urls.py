from django.urls import path
from .views import UserDetails, UserCreate, UserListView
urlpatterns = [
    path('create/', UserCreate.as_view(), name='add_user'),
    path('get/<str:pk>/', UserDetails.as_view(), name='get_user'),
    path('update/<str:pk>/', UserDetails.as_view(), name='update_user'),
    path('delete/<str:pk>/', UserDetails.as_view(), name='delete_user'),
    path('all/', UserListView.as_view(), name='user_list'),

]
