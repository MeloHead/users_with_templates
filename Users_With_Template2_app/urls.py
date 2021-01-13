from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('updated_user', views.add_user)
]
