from django.shortcuts import render
from rest_framework import generics
from crudapi.models import TeacherDetail, Qualification
from crudapi.serializers import TeacherDetailSerializer, QualificationSerializer

# Create your views here.

class TeacherDetailListView(generics.ListCreateAPIView):
    queryset = TeacherDetail.objects.all()
    serializer_class = TeacherDetailSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = TeacherDetail.objects.all()


class QualificationListView(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class QualificationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()