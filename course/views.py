from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from course.models import Stage, Subject
from course.permissions import IsModer
from course.serializers import StageSerializer, SubjectSerializer


# Create your views here.


class StageViewSet(viewsets.ModelViewSet):

    """ Класс вьюсет для модели Курс """

    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class SubjectCreateAPIView(CreateAPIView):

    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated | IsModer]


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
    permission_classes = [IsAuthenticated | IsModer]
