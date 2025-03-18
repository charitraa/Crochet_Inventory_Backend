from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path("create/", OrderAPIView.as_view(), name="order-list-create"),
    path("all/", OrderAPIView.as_view(), name="order-list-create"),

]
