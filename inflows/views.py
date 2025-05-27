from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from inflows.forms import InflowForm
from inflows.models import Inflow


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    permission_required = 'inflows.add_inflow'
    success_url = reverse_lazy('inflow_list')
