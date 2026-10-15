from django.urls import path
from register_v2.views import SignupView,BookingListCreateView
urlpatterns=[
    path("signup/",SignupView.as_view()),
    path("booking/",BookingListCreateView.as_view()),
]