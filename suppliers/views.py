from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from suppliers.forms import SupplierForm
from suppliers.models import Supplier


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    permission_required = 'suppliers.change_supplier'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    permission_required = 'suppliers.add_supplier'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    permission_required = 'suppliers.delete_supplier'
    success_url = reverse_lazy('supplier_list')