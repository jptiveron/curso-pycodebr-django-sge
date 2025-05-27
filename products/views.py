from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from products.forms import ProductForm
from products.models import Product


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 10
    permission_required = 'products.view_product'

    def queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serial_number = self.request.GET.get('serial_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if serial_number:
            queryset = queryset.filter(serial_number__icontains=serial_number)
        if category:
            queryset = queryset.filter(category__icontains=category)
        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        return queryset


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    form_class = ProductForm
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
    form_class = ProductForm
    permission_required = 'products.add_product'