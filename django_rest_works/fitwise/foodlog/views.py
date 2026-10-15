from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from foodlog.serializers import UserSerializer,foodlogSerializer
from foodlog.models import Foodlogs
from foodlog.permission import IsOwner
# Create your views here.

class SingupView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data = form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)
            serializer_instance = UserSerializer(instance)

            return Response (data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class GetmeView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        auth_user = request.user
        instance = User.objects.get(username = auth_user)
        serializer_instance = UserSerializer(instance)
        return Response(data=serializer_instance.data)

class FoodlogListCreateViews(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        instance = Foodlogs.objects.filter(owner = request.user)
        serializer_instance = foodlogSerializer(instance,many=True)
        return Response (data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = foodlogSerializer(data = form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(owner = request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class FoodlogRetrieveUpdateDeleteViews(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk = None):
        instance = get_object_or_404(Foodlogs,id=pk)
        self.check_object_permissions(request,instance)
        serializer_instance = foodlogSerializer(instance)
        return Response (data=serializer_instance.data)

    def put (self,request,pk = None):
        instance = get_object_or_404(Foodlogs,id=pk)
        self.check_object_permissions(request,instance)
        form_data = request.data
        serializer_instance = foodlogSerializer(data = form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk = None):
        instance = get_object_or_404(Foodlogs,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response(data={"message":"deleted"})


class FoodlogSummaryView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        response_data={
            "today_total":0
        }    

        cur_date = datetime.now().date()

        cur_month = datetime.now().month

        cur_year = datetime.now().year

        cur_month_calories = Foodlogs.objects.filter(owner = request.user,created_at__month = cur_month,created_at__year=cur_year)

        if cur_month_calories:

            monthly_calories = cur_month_calories.values("calories").aggregate(total=Sum("calories")).get("total")

            monthly_meal_type = cur_month_calories.values("meal_type").annotate(total = Sum("calories"))

            response_data={
                "monthly calories":monthly_calories
            }

            response_data={
                "monthly meal_type":monthly_meal_type
            }

        todays_calories = Foodlogs.objects.filter(owner=request.user,created_at__date=cur_date)

        if todays_calories:

            todays_total_calories = todays_calories.values("calories").aggregate(total=Sum("calories")).get("total")

            meal_type_summary = todays_calories.values("meal_type").annotate(total=Sum("calories"))

            response_data={
                "todays_calories":todays_total_calories
            }
            response_data={
                "meal type summary":meal_type_summary
            }

        return Response(data=response_data)