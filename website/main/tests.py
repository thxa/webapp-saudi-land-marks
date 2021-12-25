from django.test import TestCase
from .models import Landmark
from django.contrib.models import User


class LandmarkTestCase(TestCase):
    def setUp(self):
        
        Landmark(name)

    def test_landmark(self):
        """"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')