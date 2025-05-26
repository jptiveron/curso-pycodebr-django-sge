from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from brands.forms import BrandForm
from brands.models import Brand


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brand_list.html'
    paginate_by = 10
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    permission_required = 'brands.change_brand'
    success_url = reverse_lazy('brand_list')


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    permission_required = 'brands.add_brand'
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    permission_required = 'brands.delete_brand'
    success_url = reverse_lazy('brand_list')