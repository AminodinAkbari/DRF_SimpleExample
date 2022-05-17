from django.urls import path

from .views import student_list, student_save,book_Update
urlpatterns = [
    path ("student_list",student_list),
    path ("student_save",student_save),
    path ("book_Update/<pk>",book_Update.as_view()),
]