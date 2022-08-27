from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from student.serializers import StudentSerializer


class StudentList(APIView):

    def get(self, request):

        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)