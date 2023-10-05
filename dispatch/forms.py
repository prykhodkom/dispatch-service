from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from dispatch.models import Worker, Driver


def validate_phone_number(phone_number: str) -> str:
    if len(phone_number) != 12:
        raise ValidationError(
            "The phone number must contain 12 characters"
        )
    if not phone_number.startswith("+1"):
        raise ValidationError(
            "The first two characters must be '+1'"
        )
    if not phone_number[1:].isdigit():
        raise ValidationError(
            "Last 11 characters must be digits"
        )
    return phone_number


class DriverForm(forms.ModelForm):
    worker = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Driver
        fields = "__all__"

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        validate_phone_number(phone_number)
        return phone_number


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position",)


class DriverSearchForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by first name..."})
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class TruckSearchForm(forms.Form):
    type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by type..."})
    )
