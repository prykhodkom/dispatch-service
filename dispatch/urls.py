from django.urls import path

from dispatch.views import (
    index,
    DriverListView,
    WorkerListView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    TruckListView,
    TruckCreateView,
    TruckUpdateView,
    TruckDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create", PositionCreateView.as_view(), name="position-create"),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("truck/", TruckListView.as_view(), name="truck-list"),
    path("truck/create/", TruckCreateView.as_view(), name="truck-create"),
    path(
        "truck/<int:pk>/update/",
        TruckUpdateView.as_view(),
        name="truck-update"),
    path(
        "truck/<int:pk>/delete/",
        TruckDeleteView.as_view(),
        name="truck-delete"),
]

app_name = "dispatch"
