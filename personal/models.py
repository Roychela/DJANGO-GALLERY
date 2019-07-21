from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)


class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)
