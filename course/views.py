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

        if self.action in ["PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated & IsOwner, ~IsModer]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class SubjectCreateAPIView(CreateAPIView):

    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, ~IsModer]


class SubjectListAPIView(ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated & IsOwner, ~IsModer]


class SubjectRetrieveAPIView(RetrieveAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated & IsOwner, ~IsModer]


class SubjectUpdateAPIView(UpdateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated & IsOwner, ~IsModer]


class SubjectDestroyAPIView(DestroyAPIView):

    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated & IsOwner, ~IsModer]
