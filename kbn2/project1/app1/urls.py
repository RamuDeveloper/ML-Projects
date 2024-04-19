from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('products',views.products,name='products'),
    path('delete/<int:id>',views.delete_product,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('register',views.register,name="register"),
    path('login/',views.user_login,name="login"),
]