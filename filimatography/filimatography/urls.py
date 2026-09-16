"""
URL configuration for filimatography project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biography.views import MohanlalView,MammoottyView,NivinPaulyView,AsifAliView,DulquerSalmaanView
from biography.views import RanbirkapoorView,AdityaRoyKapurView,ShahRukhKhanView,RanveerSinghView,AamirKhanView
from biography.views import VijayView,SuryaView,DhanushView,KamalHaasanView,RajiniKanthView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("mohanlal/",MohanlalView.as_view()),
    path("vijay/",VijayView.as_view()),
    path("surya/",SuryaView.as_view()),
    path("mammootty/",MammoottyView.as_view()),
    path("dhanush/",DhanushView.as_view()),
    path("ranbir/",RanbirkapoorView.as_view()),
    path("aditya/",AdityaRoyKapurView.as_view()),
    path("srk/",ShahRukhKhanView.as_view()),
    path("ranveer/",RanveerSinghView.as_view()),
    path("aamir/",AamirKhanView.as_view()),
    path("kamal/",KamalHaasanView.as_view()),
    path("rajini/",RajiniKanthView.as_view()),
    path("nivin/",NivinPaulyView.as_view()),
    path("asif/",AsifAliView.as_view()),
    path("dulquer/",DulquerSalmaanView.as_view())
]
