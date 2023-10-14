from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name="index"),
    path('add',views.add,name = "add"),
    path('post/<str:pk>',views.post,name = "post"),
]