from django.test import TestCase
from .models import Location
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Paris')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_update_location(self):
        new_location_name = 'India'
        self.location.update_location(self.location.id,new_location_name)
        updated_location = Location.objects.filter(location_name='India')
        self.assertTrue(len(updated_location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)