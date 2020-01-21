from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('mydb/add/', views.data_add, name='data_add'),
    path('mydb/<int:pk>/change/', views.data_change, name='data_change'),
]
