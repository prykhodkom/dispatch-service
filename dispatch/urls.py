from django.urls import path

from dispatch.views import (
    index,
    DriverListView,
    DriverCreateView,
    DriverUpdateView,
    DriverDeleteView,
    DriverDetailView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
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
    path("driver/create", DriverCreateView.as_view(), name="driver-create"),
    path(
        "driver/<int:pk>/update/",
        DriverUpdateView.as_view(),
        name="driver-update",
    ),
    path(
        "driver/<int:pk>/delete/",
        DriverDeleteView.as_view(),
        name="driver-delete",
    ),
    path("driver/<int:pk>", DriverDetailView.as_view(), name="driver-detail"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
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
