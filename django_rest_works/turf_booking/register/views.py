from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from register.models import Booking
from register.serializers import BookingSerializer
from booking.models import TurfBook

# Create your views here.


class BookingListCreateView(APIView):

    def get(self,request):
        qs = Booking.objects.all()
        serializers_instance = BookingSerializer(qs,many = True)
        return Response(data=serializers_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = BookingSerializer(data = form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            turf = cleaned_data.get("turf")
            booking_date = cleaned_data.get("date")
            booking_time = cleaned_data.get("time")

            turf_object = TurfBook.objects.get(id=turf)
            turf_booking_object= Booking.objects.filter(turf = turf,date = booking_date,time = booking_time).last()

            if turf_booking_object:
                return Response({"message":"Turf is already booked for this date and time"})

            cleaned_data["turf"] = turf_object

            Booking.objects.create(**cleaned_data)
            response_data = {"status":"booked"}
            return Response(data= response_data)
        else:
            return Response(data=serializer_instance.errors)
            