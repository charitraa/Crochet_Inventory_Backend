from .views import PurchaseMaterialAPIView
from django.urls import path

urlpatterns = [
    path('add/', PurchaseMaterialAPIView.as_view(), name='purchase-material-list-create'),
    path('create/', PurchaseMaterialAPIView.as_view(), name='purchase-material-list-create'),
    path('delete/<str:pk>/', PurchaseMaterialAPIView.as_view(), name='purchase-material-delete'),
]