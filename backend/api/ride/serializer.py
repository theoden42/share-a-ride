from rest_framework import serializers
from .models import Ride, Passengers


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

    def update(self, instance, validated_data):
        updatable_fields = ['total_fare', 'start_datetime', 'ride_status']

        for field in updatable_fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        instance.save()
        return instance


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = '__all__'

    def update(self, instance, validated_data):

        old_status = instance.request_status
        new_status = validated_data['request_status']

        if old_status != 'Accepted' and new_status == 'Accepted':
            instance.ride.co_passengers.add(instance.user)

        setattr(instance, 'request_status', validated_data['request_status'])
        instance.save()
        return instance
