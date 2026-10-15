from django.shortcuts import render,get_object_or_404
from django.db.models import Sum
from datetime import datetime
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from spending.serializers import UserSerializer,ExpenseSerializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework import authentication,permissions
from spending.models import Expense
from spending.permission import IsOwner
from spending.ai_service import get_budget_plan

# Create your views here.

class SignUpView(APIView):

    def post(self,request):
        form_data = request.data
        serializers_instance = UserSerializer(data = form_data)

        if serializers_instance.is_valid():
            cleaned_data = serializers_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)
            serializers_instance = UserSerializer(instance)

            return Response (data=serializers_instance.data)
        else:
            return Response(data=serializers_instance.errors)

class GetmeView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        auth_user = request.user
        instance = User.objects.get(username=auth_user)
        serializer_instance = UserSerializer(instance)
        return Response(data=serializer_instance.data)

class ExpensesListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        instance = Expense.objects.filter(owner=request.user)
        serializer_instance = ExpenseSerializer(instance,many = True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = ExpenseSerializer(data = form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(owner = request.user)
            return Response(data=serializer_instance.data)

        else:
            return Response(data = serializer_instance.errors)

class ExpensesRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def get(self,request,pk=None):
        instance = get_object_or_404(Expense,id = pk)
        self.check_object_permissions(request,instance)
        serializer_instance = ExpenseSerializer(instance)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        instance = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,instance)
        form_data = request.data
        serializer_instance = ExpenseSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        instance = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response(data ={"message ":"delete"})

class ExpenseSummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(sef,request):

        response_data={
            "todays_total":0
        }

        cur_date = datetime.now().date()

        cur_month = datetime.now().month

        cur_year = datetime.now().year

        todays_transation = Expense.objects.filter(owner = request.user,created_at__date=cur_date)

        if todays_transation:

            todays_total = todays_transation.values("amount").aggregate(total=Sum("amount")).get("total")

            category_summary = todays_transation.values("category").annotate(total = Sum("amount"))


            response_data = {
                "todays_total":todays_total
            }
            response_data = {
                "category summary":category_summary
            }

        cur_month_transation = Expense.objects.filter(owner=request.user,created_at__month=cur_month,created_at__year=cur_year)
        
        if cur_month_transation:
        
            monthly_total = cur_month_transation.values("amount").aggregate(total=Sum("amount")).get("total")

            monthly_category = cur_month_transation.values("category").annotate(total=Sum("amount"))

            response_data={
                "monthly total":monthly_total
            }

            response_data = {
                "monthly category":monthly_category
            }

        return Response(data=response_data)

class BudgetPlanView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        cur_date = datetime.now().date()
        cur_month=datetime.now().month
        cur_year = datetime.now().year

        response_data ={
            "monthly_summary":0
        }
        monthly_transation = Expense.objects.filter(owner=request.user,created_at__year=cur_year,created_at__month=cur_month)
        if monthly_transation:
            monthly_total_expense=monthly_transation.values("amount").aggregate(total=Sum("amount")).get("total")
            response_data["monthly_summary"]=monthly_total_expense
            category_summary=monthly_transation.values("category").annotate(total=Sum("amount"))
            response_data["category_summary"]=category_summary
            budget_plan = get_budget_plan(response_data)
            response_data["plan"] = budget_plan
        return Response(data=response_data)
        