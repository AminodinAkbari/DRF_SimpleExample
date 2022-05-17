from django.urls import path
from .views import (
    student_delete, 
    student_detail, 
    student_list,
    student_save,
    student_update,
    register_view,
    student_List

    )
urlpatterns = [
    path('student_list', student_list),
    path('student_detail/<pk>', student_detail),
    path('student_save', student_save),
    path('student_update/<pk>', student_update),
    path('student_delete/<pk>', student_delete),

    path('register_view', register_view),
    path('student_List',student_List.as_view())


]