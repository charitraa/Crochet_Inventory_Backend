from .views import PurchaseMaterialAPIView,PurchaseDeleteView
from django.urls import path

urlpatterns = [
    path('add/', PurchaseMaterialAPIView.as_view(), name='purchase-material-list-create'),
    path('create/', PurchaseMaterialAPIView.as_view(), name='purchase-material-list-create'),
    path('delete/<str:pk>/', PurchaseDeleteView.as_view(), name='purchase-material-delete'),
    path('all/', PurchaseMaterialAPIView.as_view(), name='purchase-material-delete'),
    path('edit/<str:pk>/', PurchaseDeleteView.as_view(), name='purchase-material-update'),
    path('get/<str:pk>/', PurchaseDeleteView.as_view(), name='purchase-material-detail'),

]