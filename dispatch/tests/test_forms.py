from django.test import TestCase

from dispatch.forms import WorkerCreationForm
from dispatch.models import Position


class FormsTests(TestCase):
    def test_worker_creation_form(self):
        position = Position.object.create("Test")
        form_data = {
            "username": "driver",
            "password1": "pass123456",
            "password2": "pass123456",
            "first_name": "driver",
            "last_name": "driver",
            "position": position,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
