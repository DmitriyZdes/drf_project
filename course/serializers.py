from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Subject, Stage


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):

    subject_amount = SerializerMethodField(many=True)

    class Meta:

        model = Stage
        fields = ['name', 'preview', 'user', 'description', 'subject_amount']

    @staticmethod
    def get_subjects_amount(stage):
        return Subject.objects.filter(stage=stage).count()
