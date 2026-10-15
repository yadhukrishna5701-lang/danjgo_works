from django.urls import path

from booking_v2.views import SingupView
from booking_v2.views import AppointmentListCreateViews,AppointmentRetrieveUpdateDeleteView
urlpatterns={
    path("signup/",SingupView.as_view()),
    path("appointment/",AppointmentListCreateViews.as_view()),
    path("appointment/<int:pk>/",AppointmentRetrieveUpdateDeleteView.as_view()),
    
}