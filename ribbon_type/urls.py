from django.urls import path
from .views import ribbonView

urlpatterns = [
    path('add/', ribbonView.as_view(), name='add_view'),
    path('all/', ribbonView.as_view(), name='view_all'),
]
