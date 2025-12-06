from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .forms import VehicleForm
from .models import Vehicle, User


class RoleRequiredMixin(UserPassesTestMixin):
    """
    Generic mixin to restrict view access by user.role
    """
    allowed_roles = []

    def test_func(self):
        user = self.request.user
        return (
            user.is_authenticated
            and isinstance(user, User)
            and (user.role in self.allowed_roles)
        )


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'

    # All roles (superadmin, admin, user) can view list,


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'
    # All logged-in roles can view detail.


class VehicleCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicles:vehicle_list')

    # Only superadmin can create
    allowed_roles = [User.ROLE_SUPERADMIN]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicles:vehicle_list')

    # Super Admin + Admin can edit
    allowed_roles = [User.ROLE_SUPERADMIN, User.ROLE_ADMIN]


class VehicleDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicles:vehicle_list')

    # Only superadmin can delete
    allowed_roles = [User.ROLE_SUPERADMIN]
