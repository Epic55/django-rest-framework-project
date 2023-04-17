from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app1.serializers import StudentSerializer
from app1.models import Student

class TesView(APIView):

    permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        student1 = qa.first()
        serializer = StudentSerializer(student1)
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)