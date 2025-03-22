from django.urls import path
from .views import OrderAPIView,OrderApiViewById

urlpatterns = [
    path("create/", OrderAPIView.as_view(), name="order-list-create"),
    path("all/", OrderAPIView.as_view(), name="order-list-create"),
    path("get/<str:pk>/", OrderApiViewById.as_view(), name="order-detail"),
    path("edit/<str:pk>/", OrderApiViewById.as_view(), name="order-update"),
    path("delete/<str:pk>/", OrderApiViewById.as_view(), name="order-delete"),

]
