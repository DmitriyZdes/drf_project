from rest_framework import serializers
from course.models import Subject, Stage

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Stage
        fields = '__all__'
