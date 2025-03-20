from django.urls import path
from .views import wireTypeView

urlpatterns = [
    path('add/', wireTypeView.as_view(), name='add_view'),
    path('all/', wireTypeView.as_view(), name='view_all'),
]
