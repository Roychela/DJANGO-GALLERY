from django.test import TestCase
from .models import Location, Category
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


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Cars')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_update_category(self):
        new_category_name = 'Food'
        self.category.update_category(self.category.id,new_category_name)
        updated_category = Category.objects.filter(category_name='Food')
        self.assertTrue(len(updated_category)>0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)
