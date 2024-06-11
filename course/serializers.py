from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Subject, Stage, Subscription
from course.validators import CourseValidator


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'
        validators = [CourseValidator(field='link')]


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):

    subject_amount = SerializerMethodField()
    subject_list = SubjectSerializer(source='subject_set', many=True, read_only=True)
    subscription = SerializerMethodField()

    class Meta:

        model = Stage
        fields = ['name', 'preview', 'description', 'subject_amount', 'subject_list', 'subscription']

    @staticmethod
    def get_subject_amount(stage):
        return stage.subject_set.count()

    def get_subscription(self, obj):

        user = self.context['request'].user
        return obj.subscription_set.filter(user=user).exists()
