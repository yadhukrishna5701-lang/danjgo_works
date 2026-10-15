from django.urls import path
from foodlog.views import SingupView,GetmeView,FoodlogListCreateViews,FoodlogRetrieveUpdateDeleteViews,FoodlogSummaryView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("register/",SingupView.as_view()),
    path("me/",GetmeView.as_view()),
    path("foodlog/",FoodlogListCreateViews.as_view()),
    path("foodlog/<int:pk>/",FoodlogRetrieveUpdateDeleteViews.as_view()),   
    path("token/",ObtainAuthToken.as_view()),
    path("summary/",FoodlogSummaryView.as_view()), 

]