from django.urls import path

from dispatch.views import (
    index,
    DriverListView,
    WorkerListView,
    PositionListView,
    TypeOfTruckListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("driver/", DriverListView.as_view(), name="driver_list"),
    path("worker/", WorkerListView.as_view(), name="worker_list"),
    path("position/", PositionListView.as_view(), name="position_list"),
    path("truck/", TypeOfTruckListView.as_view(), name="type_of_truck_list"),
]

app_name = "dispatch"
