from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('qr/<int:pk>', views.details, name='details'),
]