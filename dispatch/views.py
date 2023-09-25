from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dispatch.forms import DriverForm
from dispatch.models import Worker, Driver, Truck, Position


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_drivers = Driver.objects.count()
    num_trucks = Truck.objects.count()
    num_positions = Position.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_drivers": num_drivers,
        "num_trucks": num_trucks,
        "num_position": num_positions,
        "num_visits": num_visits + 1,
    }
    return render(request, "dispatch/index.html", context=context)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 2


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("dispatch:position-list")
    template_name = "dispatch/position_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("dispatch:position-list")
    template_name = "dispatch/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("dispatch:position-list")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("dispatch:driver-list")


class DriverUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("dispatch:driver-list")


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Driver


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class TruckListView(LoginRequiredMixin, generic.ListView):
    model = Truck
    context_object_name = "truck-list"


class TruckCreateView(LoginRequiredMixin, generic.CreateView):
    model = Truck
    fields = "__all__"
    success_url = reverse_lazy("dispatch:truck-list")
    template_name = "dispatch/truck_form.html"


class TruckUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Truck
    fields = "__all__"
    success_url = reverse_lazy("dispatch:truck-list")
    template_name = "dispatch/truck_form.html"


class TruckDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Truck
    fields = "__all__"
    success_url = reverse_lazy("dispatch:truck-list")
    template_name = "dispatch/truck_confirm_delete.html"
