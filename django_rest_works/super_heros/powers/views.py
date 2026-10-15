from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from powers.models import SuperHeros
from rest_framework import serializers
# Create your views here.

class SuperHerosListCreateView(APIView):
    def get (self,request):
        qs = SuperHeros.objects.all().values()
        superhero_list = list(qs)
        return Response(data = superhero_list)

    def post(self,request):
        form_data = request.data

        powers = form_data.get("powers")

        flat = [tp[0] for tp in SuperHeros.power_options]

        if powers not in flat:
            raise serializers.ValidationError(powers+ "is not a valid choice")
        
        SuperHeros.objects.create(**form_data)

        return Response(data = {"message":"created"})

class SuperHerosRetrieveUpdateDeleteView(APIView):
    def get (self,request,pk = None):
        qs = SuperHeros.objects.filter(id=pk).values()
        power_list = list(qs)
        return Response(data = power_list)

    def put (self,request,pk = None):
        form_data = request.data
        qs = SuperHeros.objects.filter(id=pk).update(**form_data)
        return Response(data={"message":"updated..."})

    def delete(self,request,pk = None):
        SuperHeros.objects.get(id=pk).delete()
        return Response(data = {"message":"deleted"})

        