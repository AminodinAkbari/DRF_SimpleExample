from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import ListCreateAPIView

from .permissions import IsSuperUserOrReadOnly


@api_view(["GET"])#vaghti data az samt server daryaft mishavad az GET estefade mikonim
@permission_classes((IsAdminUser,))
def student_list(request):
    students = Student.objects.all()
    students_seriaizers = StudentSerializer(students,many = True)

    return Response(students_seriaizers.data)

@api_view(["GET"])
def student_detail(request,pk):
    students = Student.objects.get(id=pk)
    students_seriaizers = StudentSerializer(students,many = False)

    return Response(students_seriaizers.data)


#agar dar ghaleb json dadeh e vared shod (ghatan be soorat POST khahad bood) anra dar DB save mikonim
@api_view(["POST"])#vaghti data az samt User be Server ersal mishavad az POST estefade mikonim
def student_save(request):
    students_seriaizers = StudentSerializer(data=request.data)#tabdil kardan request az JSON be zaban ghabel fahm baraye barname
    if students_seriaizers.is_valid():
        students_seriaizers.save()
    
    return Response(students_seriaizers.data)#dade daryaft shode ra jahat namayesh ya ijad taghyir barbaye badan be soorat response barmigardanim


@api_view(["POST"])
def student_update(request,pk):
    Selected_obj = Student.objects.get(id=pk)
    students = StudentSerializer(instance=Selected_obj,data=request.data)

    if students.is_valid():
        students.save()

    return Response(students.data)

@api_view(["DELETE"])
def student_delete(request,pk):
    Selected_for_deleting = Student.objects.get(id=pk)
    Selected_for_deleting.delete()

    return Response("ROW DELETED!")

@api_view(["POST"])
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["massage"]="Register Is Done !"
            data["token"] = Token.objects.get(user=user).key
        return Response(data)


class student_List(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = ((IsSuperUserOrReadOnly,))