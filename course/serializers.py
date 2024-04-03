from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.course_modls.models import Subject, Stage


class SubjectSerializer(serializers.ModelSerializer):

    subjects_amount = SerializerMethodField()

    class Meta:

        model = Subject
        fields = '__all__'

    @staticmethod
    def get_subjects_amount():
        return Subject.objects.all().count()

class StageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Stage
        fields = '__all__'
