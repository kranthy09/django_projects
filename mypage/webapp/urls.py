from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('time_stamp/', views.time_stamp, name='time_stamp'),
    path('request_id/', views.unique_id, name='unique_id'),
    path('home_page/', views.home_page, name='home_page'),
]