from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Subject, Stage


class SubjectSerializer(serializers.ModelSerializer):

    subjects_amount = SerializerMethodField()

    class Meta:

        model = Subject
        fields = ['stage', 'name', 'preview', 'user', 'description', 'subjects_amount']

    @staticmethod
    def get_subjects_amount():
        return Subject.objects.all().count()

class StageSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(read_only=True)

    class Meta:

        model = Stage
        fields = ['name', 'preview', 'user', 'description', 'subject']
