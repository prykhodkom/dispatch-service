from django.urls import path

from dispatch.views import (
    index,
    DriverListView,
    WorkerListView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    TypeOfTruckListView,
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
    path("truck/", TypeOfTruckListView.as_view(), name="type-of-truck-list"),
]

app_name = "dispatch"
