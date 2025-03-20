from django.urls import path
from .views import yarnTypeView

urlpatterns = [
    path('add/', yarnTypeView.as_view(), name='add_view'),
    path('all/', yarnTypeView.as_view(), name='view_all'),
]
