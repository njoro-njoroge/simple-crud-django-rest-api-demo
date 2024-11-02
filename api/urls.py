
from django.urls import path
from .views import get_products,create_product, product_details


urlpatterns = [
    path('products/', get_products, name='get_product'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:pk>/', product_details, name='product_details'),
]

