from django.shortcuts import render
from rest_framework import viewsets
from app.models import StudentModel
from app.serializers import StudentSerializers

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers