from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from register_v2.seralizers import SignupSerializer,BookingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from register_v2.models import Booking
from datetime import time
from datetime import datetime
from datetime import timedelta

class SignupView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = SignupSerializer(data = form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            user_object = User.objects.create_user(**cleaned_data)
            ser_inst = SignupSerializer(user_object)
            return Response(data = ser_inst.data)
        else:
            return Response(data = serializer_instance.errors)

class BookingListCreateView(APIView):
    def get (self,request):
        qs = Booking.objects.all()
        serializer_instance = BookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = BookingSerializer(data = form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data

            turf = cleaned_data.get("turf")
            booking_date = cleaned_data.get("date")
            booking_time = cleaned_data.get("time")
            duration = cleaned_data.get("duration")

            start = datetime.combine(booking_date,booking_time)
            end = start+timedelta(hours=duration)

            last_booking_object = Booking.objects.filter(turf = turf,date = booking_date).last()

            if last_booking_object:

                last_booking_start_object = datetime.combine(last_booking_object.date,last_booking_object.time)
                last_booking_end_object = last_booking_start_object+timedelta(hours=last_booking_object.duration)

                if start < last_booking_end_object and end > last_booking_start_object:

                    raise serializers.ValidationError("another team already booked in this time")

            qs = Booking.objects.create(**cleaned_data)
            serializer_instance = BookingSerializer(qs)

            return Response(data = serializer_instance.data)
        else:
                return Response(data = serializer_instance.errors)   
                