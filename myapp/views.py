from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Book
# Create your views here.


def index(request):
    return HttpResponse("Hello Django World")


def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request,'bookdetails.html',{"book":book})
