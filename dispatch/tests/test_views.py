from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dispatch.models import Driver, Position, Truck, Worker

DRIVERS_URL = reverse("dispatch:driver-list")
POSITIONS_URL = reverse("dispatch:position-list")
TRUCKS_URL = reverse("dispatch:truck-list")
WORKERS_URL = reverse("dispatch:worker-list")


class PublicPositionTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(POSITIONS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "testpassword1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(type="test", lenght=48, max_weight=40000)
        Position.objects.create(type="test1", lenght=26, max_weight=10000)

        response = self.client.get(POSITIONS_URL)
        positions = Position.objects.all()
        self.assertEquals(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(response, "dispatch/position_list.html")


class PublicTruckTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(TRUCKS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateTruckTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "testpassword1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_truck(self):
        Truck.objects.create(type="test", lenght=48, max_weight=40000)
        Truck.objects.create(type="test1", lenght=26, max_weight=10000)

        response = self.client.get(TRUCKS_URL)
        trucks = Truck.objects.all()
        self.assertEquals(response.status_code, 200)
        self.assertEqual(
            list(response.context["truck_list"]),
            list(trucks)
        )
        self.assertTemplateUsed(response, "dispatch/truck_list.html")


class PublicDriverTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(DRIVERS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDriverTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "testpassword1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_driver(self):
        truck = Truck.objects.create(type="test", lenght=48, max_weight=40000)
        Driver.objects.create(
            first_name="test",
            last_name="test",
            phone_number="+13465297568",
            home_location="Atlanta, GA",
            type_of_truck=truck,
        )

        response = self.client.get(DRIVERS_URL)
        drivers = Driver.objects.all()
        self.assertEquals(response.status_code, 200)
        self.assertEqual(
            list(response.context["driver_list"]),
            list(drivers)
        )
        self.assertTemplateUsed(response, "dispatch/driver_list.html")


class PublicWorkerTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(WORKERS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpassword`1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_worker(self):
        Worker.objects.create(username="Test")
        response = self.client.get(WORKERS_URL)
        workers = Worker.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(response, "dispatch/worker_list.html")
