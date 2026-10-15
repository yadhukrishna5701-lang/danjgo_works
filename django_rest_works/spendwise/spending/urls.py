from django.urls import path
from spending.views import SignUpView,GetmeView,ExpensesListCreateView,ExpensesRetrieveUpdateDeleteView
from rest_framework.authtoken.views import ObtainAuthToken
from spending.views import ExpenseSummaryView,BudgetPlanView
urlpatterns = [
    path("register/",SignUpView.as_view()),
    path("me/",GetmeView.as_view()),
    path("expenses/",ExpensesListCreateView.as_view()),
    path("expenses/<int:pk>/",ExpensesRetrieveUpdateDeleteView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("summary/",ExpenseSummaryView.as_view()),
    path("budget/",BudgetPlanView.as_view()),
]