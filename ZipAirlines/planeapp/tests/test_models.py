from django.test import TestCase
from planeapp.models import Airplane

class AirplaneTest(TestCase):


    def setUp(self):
        self.airplane = Airplane(plane_id = "1", pass_no = "100")


    def test_tank_capacity(self):
        """
        Tests tank capacity property
        """
        self.assertEqual(str(self.airplane.tank_capacity), "200")

    def test_pass_consuption(self):
        """
        Tests passanger consuption property
        """
        self.assertEqual(str(self.airplane.pass_consuption), "0.2")

    def test_fuel_consuption_min(self):
        """
        Tests total fuel consuption per minute property
        """
        self.assertEqual(str(self.airplane.fuel_consuption_min), "1.0")

    def test_fly_time(self):
        """
        Tests maximum flying time property
        """        
        self.assertEqual(str(self.airplane.fly_time), "200.0")
