from django.contrib.auth import get_user_model
from django.test import TestCase

from dispatch.models import Driver, Position, Truck, Worker


class ModelsTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="Test",
        )
        self.assertEqual(
            str(position), f"{position.name}"
        )

    def test_truck_str(self):
        truck = Truck.objects.create(
            type="Test",
            length=53,
            max_weight=50000,
        )
        self.assertEqual(
            str(truck), f"{truck.type} with length: {truck.length}' and max weight: {truck.max_weight} lbs"
        )

    def test_driver_str(self):
        driver = Driver.objects.create_user(
            first_name="Mykhailo",
            last_name="Prykhodko",
            phone_number="+14678954856"
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_worker_str(self):
        worker = get_user_model().objects.create_user(
            username="m.prykhodko",
            first_name="Mykhailo",
            last_name="Prykhodko",
            password="test12345"
        )

        self.assertEqual(
            str(worker),
            f"{worker.first_name} {worker.last_name}"
        )
