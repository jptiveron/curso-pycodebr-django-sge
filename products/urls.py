from django.urls import path
from products.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/detail', ProductDetailView.as_view(), name='product_detail'),
]