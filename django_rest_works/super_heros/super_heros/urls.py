"""
URL configuration for super_heros project.

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
from powers.views import SuperHerosListCreateView
from powers.views import SuperHerosRetrieveUpdateDeleteView
from powers_v2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powers/',SuperHerosListCreateView.as_view()),
    path("powers/<int:pk>/",SuperHerosRetrieveUpdateDeleteView.as_view()),
    path("v2/powers/",views.SuperHeroListCreateView.as_view()),
    path("v2/powers/<int:pk>/",views.SuperHeroRetrieveUpdateDeleteView.as_view()),
]
