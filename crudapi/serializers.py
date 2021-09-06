from rest_framework import serializers
from crudapi.models import TeacherDetail, Qualification

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'teacher', 'ssc', 'hsc', 'honours', 'master', 'extra')

class TeacherDetailSerializer(serializers.ModelSerializer):
    qualifications = QualificationSerializer(many=True)
    class Meta:
        model = TeacherDetail
        fields = ('id', 'name', 'email', 'phone', 'institute', 'experience', 'address', 'qualifications', 'linkedin')

    def create(self, validated_data):
        qualifications_data = validated_data.pop('qualifications')
        teacherDetail = TeacherDetail.objects.create(**validated_data)
        for qualification_data in qualifications_data:
            Qualification.objects.create(teacher=teacherDetail, **qualification_data)
        return teacherDetail
    
    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.institute = validated_data.get('institute', instance.institute)
    #     instance.experience = validated_data.get('experience', instance.experience)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.qualifications = validated_data.get('qualifications', instance.qualifications)
    #     instance.linkedin = validated_data.get('linkedin', instance.linkedin)
    #     instance.save()
    #     return instance