from django.shortcuts import render
from django.views.generic import View
from crm.models import Empolyee
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreaateView(View):

    def get(self,request):

        qs = Empolyee.objects.all().values()

        employee_list = list(qs)

        return JsonResponse(employee_list,safe=False)

    
    def post(self,request):

        form_data = loads(request.body)

        Empolyee.objects.create(
            name = form_data.get("name"),
            department = form_data.get("department"),
            salary=form_data.get("salary"),
            location=form_data.get("location"),
            email=form_data.get("email") 
                )

        response_data = {"message":"employee created"}

        return JsonResponse(response_data,safe=False)

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):
        qs = Empolyee.objects.filter(id=pk).values()

        emp_list = list(qs)

        return JsonResponse(emp_list,safe=False)

    def delete(self,request,pk=None):
        qs = Empolyee.objects.get(id=pk).delete()

        response_data = {"message":"record deleted"}
        return JsonResponse(response_data)

    def put(self,request,pk =None):
        form_data = loads(request.body)
        Empolyee.objects.filter(pk=2).update(**form_data)

        response_data={"message":"updated..."}
        return JsonResponse(response_data)