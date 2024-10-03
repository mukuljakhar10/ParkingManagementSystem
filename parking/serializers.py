from rest_framework import serializers
from .models import ParkingSpace, ParkingHistory

class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'

    def validate_level(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("Level must be between 0 and 10")
        return value

class ParkingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingHistory
        fields = ['level', 'type', 'vehicle_number', 'lot', 'fee', 'check_in', 'check_out']
