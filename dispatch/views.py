from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dispatch.models import Worker, Driver, TypeOfTruck, Position


def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_drivers = Driver.objects.count()
    num_trucks = TypeOfTruck.objects.count()
    num_positions = Position.objects.count()
    context = {
        "num_workers": num_workers,
        "num_drivers": num_drivers,
        "num_trucks": num_trucks,
        "num_position": num_positions,
    }
    return render(request, "dispatch/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position
    paginate_by = 2


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("dispatch:position-list")
    template_name = "dispatch/position_form.html"


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("dispatch:position-list")
    template_name = "dispatch/position_form.html"


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("dispatch:position-list")


class DriverListView(generic.ListView):
    model = Driver


class WorkerListView(generic.ListView):
    model = Worker


class TypeOfTruckListView(generic.ListView):
    model = TypeOfTruck
    template_name = "dispatch/type_of_truck_list.html"
    context_object_name = "type-of-truck-list"
