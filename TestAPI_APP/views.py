from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
import requests
import json

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Book
from Student.serializers import BookSerializer
from .permissions import IsAuthor
# Create your views here.

def student_list(request):
    response_obj = requests.get("http://127.0.0.1:8000/students/student_list").json()#convert to json
    context = {
        "obj" : response_obj
    }

    return render(request,"student_list.html",context)


def student_save(request):#create a student with apis
    instance = {
        "name":"رضا",
        "family":"اکبری",
        "code" : "10"
    }#make fields
    to_json = json.dumps(instance)#tabdil va ersal instance static ya dynamic be vasile json.dumbs 
    header = {"content-type":"application/json"}#taein noe header be vasile content-type(requairment)

    requests.post("http://127.0.0.1:8000/students/student_save",data=to_json,headers=header)#bayad data va header ra baraye requests.post ersal konim

    return redirect(student_list)

class book_Update(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = ((IsAuthor,))