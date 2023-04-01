from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.testGetProducts, name="getProducts"),
    path('products/<int:id>/', views.testGetProduct, name="getProduct"),
    path('categories/', views.testGetCategories, name="getCategories"),
    path('categories/<int:id>/', views.testGetCategory, name="getCategory"),
    path('categories/<int:id>/products', views.testGetProductByCategory, name="getProductByCategory"),
]