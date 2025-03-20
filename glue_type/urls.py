from django.urls import path
from .views import glueView

urlpatterns = [
    path('add/', glueView.as_view(), name='add_view'),
    path('all/', glueView.as_view(), name='view_all'),
]
