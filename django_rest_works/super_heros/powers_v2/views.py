from django.shortcuts import render
from rest_framework.views import APIView
from powers_v2.serialisers import SuperHerosSerializer
from rest_framework.response import Response
from powers.models import SuperHeros
# Create your views here.

class SuperHeroListCreateView(APIView):
    def get (self,request):
        qs = SuperHeros.objects.all()
        serializer_instance = SuperHerosSerializer(qs,many=True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = SuperHerosSerializer(data = form_data)
        if serializer_instance.is_valid():
            cleared_data = serializer_instance.validated_data
            SuperHeros.objects.create(**cleared_data)
            return Response(serializer_instance.validated_data)
        else:
            return Response(serializer_instance.errors)

class SuperHeroRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk = None):
        qs = SuperHeros.objects.get(id=pk)
        serializer_instance = SuperHerosSerializer(qs)
        return Response (data = serializer_instance.data)
        