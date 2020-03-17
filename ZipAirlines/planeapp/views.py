from django.shortcuts import render
from planeapp.serializers import AirplaneSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from planeapp.models import Airplane
from rest_framework.throttling import AnonRateThrottle
# Create your views here.


class AirplaneView(APIView):

    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        """
        Lists all previous entries and calculations
        """
        queryset = Airplane.objects.all()
        serializer = AirplaneSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create new calcualtions based on inputs
        """
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
