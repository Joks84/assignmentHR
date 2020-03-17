from rest_framework import serializers
from planeapp.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ('plane_id', 'pass_no', 'tank_capacity', 'pass_consuption',
                    'fuel_consuption_min', 'fly_time')
