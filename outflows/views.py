from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from outflows.forms import OutflowForm
from outflows.models import Outflow


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_list.html'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    permission_required = 'outflows.add_outflow'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')
