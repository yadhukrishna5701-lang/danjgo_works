from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        respones_data = {"message":"helloworld"}
        return JsonResponse(respones_data)
    
class GoodMorningView(View):
    def get(self,request):
        respones_data = {"message":"goodmorning"}
        return JsonResponse(respones_data)

class GoodAfternoonView(View):
    def get(self,request):
        response_data = {"message":"goodafternoon"}
        return JsonResponse(response_data)

class GoodEveningView(View):
    def get(self,request):
        response_data = {"message":"goodevening"}
        return JsonResponse(response_data)

class GoodNightView(View):
    def get(self,request):
        respones_data = {"message":"goodnight"}
        return JsonResponse(respones_data)