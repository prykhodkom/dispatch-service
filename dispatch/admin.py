from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Worker, Truck, Position

# Register your models here.


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(Driver)
admin.site.register(Position)
admin.site.register(Truck)
