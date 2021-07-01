from django.urls import path, include
from .views import affiliate_list

urlpatterns = [
    path('affiliates/', affiliate_list, name='affiliates'),
]