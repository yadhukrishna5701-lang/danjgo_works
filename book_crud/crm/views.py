from django.shortcuts import render
from django.views.generic import View
from crm.models import Book
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class BookListCreateView(View):
    def get (self,request):

        qs = Book.objects.all().values()
        book_list = list(qs)

        return JsonResponse(book_list,safe=False)

    def post(self,request):

        form_data = loads(request.body)
        Book.objects.create(
            title = form_data.get("title"),
            author = form_data.get("author"),
            price = form_data.get("price"),
            pages = form_data.get("pages"),
            publication = form_data.get("publication")
        )

        response_data ={"message":"book created"}
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class BookRetieveUpdateDeleteView(View):
    def get(self,request,pk=None):
        qs = Book.objects.filter(id=pk).values()
        Book_list = list(qs)

        return JsonResponse(Book_list,safe=False)

    def delete(self,request,pk=None):
        Book.objects.get(id=pk).delete()
        response_data = {"mesage":"book deleted"}
        return JsonResponse(response_data)

