from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from crudapi.models import TeacherDetail
from crudapi.serializers import TeacherDetailSerializer
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