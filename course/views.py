from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Stage, Subject, Subscription
from course.paginators import SubjectPagination, StagePagination
from course.permissions import IsModer, IsOwner
from course.serializers import StageSerializer, SubjectSerializer, SubscriptionSerializer


# Create your views here.


class StageViewSet(viewsets.ModelViewSet):

    """ Класс вьюсет для модели Курс """

    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    pagination_class = StagePagination

    def get_permissions(self):

        if self.action in ["GET", "POST"]:
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ["PUT", "PATCH"]:
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


class SubjectCreateAPIView(CreateAPIView):

    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, ~IsModer]


class SubjectListAPIView(ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SubjectPagination


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
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionAPIView(APIView):

    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):

        user = self.request.user
        stage_id = self.request.data.get("stage")
        stage_item = get_object_or_404(Stage, pk=stage_id)
        subs_item = Subscription.objects.all().filter(user=user).filter(stage_item=stage_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'

        else:
            Subscription.objects.create(user=user, stage_item=stage_item)
            message = 'подписка добавлена'
        return Response({'message': message})
