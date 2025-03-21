from django.urls import path
from .views import UserDetails, UserCreate, UserListView, UpdateProfileIcon,UserUpdateProfile

urlpatterns = [
    # Endpoint to create a new user
    path('create/', UserCreate.as_view(), name='add_user'),
    
    # Endpoint to retrieve details of a specific user by their primary key (pk)
    path('get/<str:pk>/', UserDetails.as_view(), name='get_user'),
    
    # Endpoint to update a specific user's details by their primary key (pk)
    path('update/<str:pk>/', UserDetails.as_view(), name='update_user'),
    
    # Endpoint to delete a specific user by their primary key (pk)
    path('delete/<str:pk>/', UserDetails.as_view(), name='delete_user'),
    
    # Endpoint to retrieve a list of all users
    path('all/', UserListView.as_view(), name='user_list'),

    # Endpoint to update a user's profile picture
    path('update-profile-icon/', UpdateProfileIcon.as_view(), name='update_profile_icon'),
    path('update-profile/', UserUpdateProfile.as_view(), name='update_profile'),

]
