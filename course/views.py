from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from course.models import Stage, Subject
from course.serializers import StageSerializer, SubjectSerializer


# Create your views here.


class StageViewSet(viewsets.ViewSet):

    """ Класс вьюсет для модели Курс """

    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class SubjectCreateAPIView(CreateAPIView):

    serializer_class = SubjectSerializer


class SubjectListAPIView(ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectRetrieveAPIView(RetrieveAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectUpdateAPIView(UpdateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectDestroyAPIView(DestroyAPIView):

    queryset = Subject.objects.all()
