from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='products-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy')
]