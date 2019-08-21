from django.test import TestCase
from .models import Prepaidplans

# Create your tests here.
class Prepaidplans(TestCase):
    def setUp(self):
        Prepaidplans.objects.create(
            name="699",
            price="699",
            des="unlimited plans",
            
        )
