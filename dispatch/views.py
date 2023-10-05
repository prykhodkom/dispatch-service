from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dispatch.forms import DriverForm, WorkerCreationForm, WorkerSearchForm, TruckSearchForm, PositionSearchForm, \
    DriverSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("type", "")

        context["search_form"] = PositionSearchForm(initial={
            "name": name,
        })

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Position.objects.select_related("manufacturer")

        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return Position.objects.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DriverListView, self).get_context_data(**kwargs)

        first_name = self.request.GET.get("first_name", "")

        context["search_form"] = DriverSearchForm(initial={
            "first_name": first_name,
        })

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Driver.objects.select_related("manufacturer")

        form = DriverSearchForm(self.request.GET)

        if form.is_valid():
            return Driver.objects.filter(
                first_name__icontains=form.cleaned_data["first_name"]
            )

        return queryset


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
    success_url = reverse_lazy("dispatch:driver-list")


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(initial={
            "username": username,
        })

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Worker.objects.select_related("manufacturer")

        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return Worker.objects.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("dispatch:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = ("first_name", "last_name", "position",)
    success_url = reverse_lazy("dispatch:worker-list")
    template_name = "dispatch/worker_form.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("dispatch:worker-list")
    template_name = "dispatch/worker_confirm_delete.html"


class TruckListView(LoginRequiredMixin, generic.ListView):
    model = Truck
    context_object_name = "truck-list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TruckListView, self).get_context_data(**kwargs)

        type_ = self.request.GET.get("type", "")

        context["search_form"] = TruckSearchForm(initial={
            "type": type_,
        })

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Truck.objects.select_related("manufacturer")

        form = TruckSearchForm(self.request.GET)

        if form.is_valid():
            return Truck.objects.filter(
                type__icontains=form.cleaned_data["type"]
            )

        return queryset


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
    success_url = reverse_lazy("dispatch:truck-list")
    template_name = "dispatch/truck_confirm_delete.html"
