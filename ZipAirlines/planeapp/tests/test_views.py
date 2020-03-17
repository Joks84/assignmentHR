import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from planeapp.models import Airplane
from planeapp.serializers import AirplaneSerializer

client = Client()

class AirplanesTest(TestCase):

    def setUp(self):
        self.airplane = {"plane_id":1, "pass_no":100}

    def test_get_plane(self):
        """
        Tests GET request
        """
        response = client.get(reverse('plane'))
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_plane(self):
        """
        Tests POST request
        """
        response = client.post(reverse('plane'),
            data = json.dumps(self.airplane),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
