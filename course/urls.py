from django.urls import path
from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig
from course.views import (StageViewSet, SubjectCreateAPIView, SubjectListAPIView, SubjectRetrieveAPIView,
                          SubjectUpdateAPIView, SubjectDestroyAPIView, SubscriptionAPIView)

app_name = CourseConfig.name


router = DefaultRouter()
router.register(r'stage', StageViewSet)

urlpatterns = [
    path('course/create/', SubjectCreateAPIView.as_view(), name='create_course'),
    path('course/', SubjectListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', SubjectRetrieveAPIView.as_view(), name='get_course'),
    path('course/update/<int:pk>/', SubjectUpdateAPIView.as_view(), name='update_course'),
    path('course/delete/<int:pk>/', SubjectDestroyAPIView.as_view(), name='delete_course'),
    path('api-view/', SubscriptionAPIView.as_view(), name='subscription_appearance'),

]

urlpatterns += router.urls
