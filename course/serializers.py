from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Subject, Stage


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):

    subject_amount = SerializerMethodField()
    subject_list = SubjectSerializer(source='subject_set', many=True, read_only=True)

    class Meta:

        model = Stage
        fields = ['name', 'preview', 'description', 'subject_amount', 'subject_list']

    @staticmethod
    def get_subject_amount(stage):
        return stage.subject_set.count()
