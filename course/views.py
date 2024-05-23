from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from course.models import Stage, Subject
from course.permissions import IsModer, IsOwner
from course.serializers import StageSerializer, SubjectSerializer


# Create your views here.


class StageViewSet(viewsets.ModelViewSet):

    """ Класс вьюсет для модели Курс """

    queryset = Stage.objects.all()
    serializer_class = StageSerializer

    def get_permissions(self):

        if self.action in ["GET", "POST"]:
            self.permission_classes = [IsAuthenticated, IsModer, IsOwner]
        elif self.action in ["PUT", "PATCH"]:
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner, ~IsModer]
        return super().get_permissions()


class SubjectCreateAPIView(CreateAPIView):

    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsModer, IsOwner]


class SubjectListAPIView(ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsModer, IsOwner]


class SubjectRetrieveAPIView(RetrieveAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class SubjectUpdateAPIView(UpdateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class SubjectDestroyAPIView(DestroyAPIView):

    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, ~IsModer]
