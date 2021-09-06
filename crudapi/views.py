from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from crudapi.models import TeacherDetail, Qualification
from crudapi.serializers import TeacherDetailSerializer, QualificationSerializer
# Create your views here.

@api_view(["GET"])
def get_teacherinfo(request):
    teacherDetail = TeacherDetail.objects.all()
    serializer = TeacherDetailSerializer(teacherDetail, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_teacherinfo_detail(request, pk):
    teacherDetail = TeacherDetail.objects.get(id=pk)
    serializer = TeacherDetailSerializer(teacherDetail, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def post_teacherinfo(request):
    serializer = TeacherDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def post_teacherinfo_detail(request, pk):
    teacherDetail = TeacherDetail.objects.get(id=pk)
    serializer = TeacherDetailSerializer(instance=teacherDetail, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_teacherinfo(request, pk):
    teacherDetail = TeacherDetail.objects.get(id=pk)
    serializer = TeacherDetailSerializer(instance=teacherDetail, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_teacherinfo(request, pk):
    teacherDetail = TeacherDetail.objects.get(id=pk)
    teacherDetail.delete()
    return Response('Delete Successfully')

# Qualification

@api_view(["GET"])
def get_qualification(request):
    qualification = Qualification.objects.all()
    serializer = QualificationSerializer(qualification, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_qualification_detail(request, pk):
    qualification = Qualification.objects.get(id=pk)
    serializer = QualificationSerializer(qualification, many=False)
    return Response(serializer.data)   

@api_view(["POST"])
def post_qualification(request):
    serializer = QualificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def post_qualification_detail(request, pk):
    qualification = Qualification.objects.get(id=pk)
    serializer = QualificationSerializer(instance=qualification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



@api_view(['PUT'])
def update_qualification(request, pk):
    qualification = Qualification.objects.get(id=pk)
    serializer = QualificationSerializer(instance=qualification, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_qualification(request, pk):
    qualification = Qualification.objects.get(id=pk)
    qualification.delete()
    return Response('Delete Successfully')