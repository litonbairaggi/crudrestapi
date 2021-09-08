from rest_framework import serializers, fields
from crudapi.models import TeacherDetail, Qualification

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'teacher', 'ssc', 'hsc', 'honours', 'master', 'extra')

class TeacherDetailSerializer(serializers.ModelSerializer):
    teacher_qualifications = QualificationSerializer(many=True)
    class Meta:
        model = TeacherDetail
        fields = ('id', 'name', 'email', 'phone', 'institute', 'experience', 'address', 'linkedin', 'teacher_qualifications')

    def create(self, validated_data):
        qualifications_data = validated_data.pop('teacher_qualifications')
        teacherDetail = TeacherDetail.objects.create(**validated_data)
        for qualification_data in qualifications_data:
            Qualification.objects.create(teacher=teacherDetail, **qualification_data)
        return teacherDetail

    def update(self, instance, validated_data):
        qualifications_data = validated_data.pop('teacher_qualifications')
        qualifications = (instance.teacher_qualifications).all()
        qualifications = list(qualifications)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.institute = validated_data.get('institute', instance.institute)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.address = validated_data.get('address', instance.address)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.save()


        for qualification_data in qualifications_data:
            qualification = qualifications.pop(0)
            qualification.ssc = qualification_data.get('ssc', qualification.ssc)
            qualification.hsc = qualification_data.get('hsc', qualification.hsc)
            qualification.honours = qualification_data.get('honours', qualification.honours)
            qualification.master = qualification_data.get('master', qualification.master)
            qualification.extra = qualification_data.get('extra', qualification.extra)
            qualification.save()
        return instance