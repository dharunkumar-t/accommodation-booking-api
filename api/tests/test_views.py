from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Property, Booking
from django.contrib.auth.models import User
from decimal import Decimal

class PropertyViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.property = Property.objects.create(
            owner=self.user,
            title='Test Property',
            description='A test property description',
            price_per_night=Decimal('100.00'),
            location='Test Location'
        )

    def test_get_property_list(self):
        response = self.client.get(reverse('property-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookingViewSetTest(APITestCase):
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

    def test_get_booking_list(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
