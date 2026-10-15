from rest_framework import serializers
from django.contrib.auth.models import User
from register_v2.models import Booking
from datetime import datetime
# Create your views here.


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

        read_only_fields = ["id","created_at"]

    def validate(self, validated_data):
        booking_date = validated_data.get("date")
        turf = validated_data.get("turf")
        booking_time = validated_data.get("time")
        if booking_date < datetime.today().date():
            raise serializers.ValidationError("date should be grater than current date")

        last_booking_object = Booking.objects.filter(turf = turf, booking_date = booking_date).last()

        if last_booking_object:
            if last_booking_object.time in booking_time:
                raise serializers.ValidationError("slot alrdy booked in this time")

        return validated_data


