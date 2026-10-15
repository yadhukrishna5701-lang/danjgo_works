from django.shortcuts import render
from rest_framework.views import APIView
from booking.models import TurfBook
from booking_v2.serializers import TurfBookSerializer,UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
# Create your views here.


class AdminCreateView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data = form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            User.objects.create_superuser(**cleaned_data)
            return Response(serializer_instance.validated_data)
        else:
            return Response(serializer_instance.errors)
        
class TurfCreateListView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self,request):
        qs = TurfBook.objects.all()
        serializer_instance = TurfBookSerializer(qs,many = True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = TurfBookSerializer(data = form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            TurfBook.objects.create(**cleaned_data)
            return Response(serializer_instance.validated_data)
        else:
            return Response(serializer_instance.errors)

class TurfRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self,request,pk = None):
        qs = TurfBook.objects.get(id=pk)
        serializer_instance = TurfBookSerializer(qs)
        return Response (data = serializer_instance.data)

    def put(self,request,pk = None):
        form_data = request.data
        serializer_instance = TurfBookSerializer(data = form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            TurfBook.objects.filter(id=pk).update(**cleaned_data)
            return Response(serializer_instance.validated_data)
        else:
            return Response (serializer_instance.errors)

    def delete (self,request,pk = None):
        qs = TurfBook.objects.get(id=pk).delete()
        serializer_instance = TurfBookSerializer(qs)
        return Response(data = serializer_instance.data)