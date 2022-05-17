from rest_framework import serializers

from TestAPI_APP.models import Book
from .models import Student
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"