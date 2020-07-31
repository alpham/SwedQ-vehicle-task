from django.test import TestCase
from vehicles_demo.apps.vehicles.models import Customer, Vehicles

class TestSearch(TestCase):
    fixtures = [
        'customers.json',
        'vehicles.json'
    ]
    
    def setUp(self):
        self.customer = Customer.objects.first()

    def test_search_per_customer_name(self):
        response = self.client.get('/search/?customer_name={}'.format(self.customer.name))
        self.assertEquals(len(response.json()), self.customer.vehicles.all().count())
    
    def test_search_per_vehicle_status(self):
        response = self.client.get('/search/?online=true')
        self.assertEquals(len(response.json()), Vehicles.objects.filter(online=True).count())
    
    def test_search_per_vehicle_status_and_customer_name(self):
        response = self.client.get('/search/?online=true&customer_name={}'.format(self.customer.name))
        self.assertEquals(
                    len(response.json()), 
                    Vehicles.objects.filter(
                            online=True, 
                            customer__name__contains=self.customer.name
                        ).count())