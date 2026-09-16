from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class MohanlalView(View):
    def get (self,request):
        respones_data = {
            "name":"mohanlal",
            "language":"malayalam",
            "movies": "500"
        }
        return JsonResponse(respones_data)

class VijayView(View):
    def get(self,request):
        respone_data = {
            "name":"vijay",
            "language":"tamil",
            "movies": "69"
        }
        return JsonResponse(respone_data)

class SuryaView(View):
    def get(self,request):
        respone_data = {
            "name":"surya",
            "language":"tamil",
            "movies": "50"
        }
        return JsonResponse(respone_data)

class MammoottyView(View):
    def get(self,request):
        respone_data ={
            "name":"mammootty",
            "language":"malayalam",
            "movie":"100"
        }
        return JsonResponse(respone_data)

class DhanushView(View):
    def get(self,request):
        respones_data = {
            "name":"dhanush",
            "language":"tamil",
            "movies":"30"
        }
        return JsonResponse(respones_data)

class RanbirkapoorView(View):
    def get(self,request):
        respones_data = {
            "name":"ranbir kapoor",
            "language":"hindi",
            "movies":"25"
        }
        return JsonResponse(respones_data)

class AdityaRoyKapurView(View):
    def get (self,request):
        respones_dat = {
            "name":"aditya roy kapur",
            "language":"hindi",
            "movies":"30"
        }
        return JsonResponse(respones_dat)

class ShahRukhKhanView(View):
    def get(self,request):
        respones_data = {
            "name":"shah rukn khan",
            "language":"hindi",
            "movies":"100"
        }
        return JsonResponse(respones_data)

class RanveerSinghView(View):
    def get(self,request):
        respones_data ={
            "name":"ranveer singh",
            "language":"hindi",
            "movies":"25"
        }
        return JsonResponse(respones_data)

class AamirKhanView(View):
    def get(self,request):
        respones_data={
            "name":"aamir khan",
            "language":"hindi",
            "movies":"40"
        }
        return JsonResponse(respones_data)

class KamalHaasanView(View):
    def get(self,request):
        respones_data={
            "name":"kamal haasan",
            "language":"tamil",
            "movies":"110"
        }
        return JsonResponse(respones_data)

class RajiniKanthView(View):
    def get(self,request):
        respones_data = {
            "name":"rajini kanth",
            "language":"tamil",
            "movies":"105"
        }
        return JsonResponse(respones_data)

class NivinPaulyView(View):
    def get(seld,request):
        respones_data = {
            "name":"nivin pauly",
            "language":"malayalam",
            "movies":"40"
        }
        return JsonResponse(respones_data)

class AsifAliView(View):
    def get(self,request):
        respones_data = {
            "name":"asif ali",
            "language":"malayalam",
            "movies":"45"
        }
        return JsonResponse(respones_data)

class DulquerSalmaanView(View):
    def get (self,request):
        respones_data = {
            "name":"dulquer salmaan",
            "landuage":"malayalam",
            "movies":"40"
        }
        return JsonResponse(respones_data)
    