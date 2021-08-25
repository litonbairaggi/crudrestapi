from rest_framework import serializers
from crudapi.models import TeacherDetail

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetail
        fields = '__all__'