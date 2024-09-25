from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Property, Booking
from decimal import Decimal

class PropertyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.property = Property.objects.create(
            owner=self.user,
            title='Test Property',
            description='A test property description',
            price_per_night=Decimal('100.00'),
            location='Test Location'
        )

    def test_property_creation(self):
        self.assertTrue(isinstance(self.property, Property))
        self.assertEqual(self.property.__str__(), self.property.title)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.property = Property.objects.create(
            owner=self.user,
            title='Test Property',
            description='A test property description',
            price_per_night=Decimal('100.00'),
            location='Test Location'
        )
        self.booking = Booking.objects.create(
            property=self.property,
            guest=self.user,
            check_in_date='2023-01-01',
            check_out_date='2023-01-05',
            total_price=Decimal('400.00')
        )

    def test_booking_creation(self):
        self.assertTrue(isinstance(self.booking, Booking))
        self.assertEqual(self.booking.__str__(), f"{self.user.username} - {self.property.title}")
