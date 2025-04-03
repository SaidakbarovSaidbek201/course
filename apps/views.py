from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import User,  Course, Lesson, Enrollment
from .serializers import UserSerializer, CourseSerializer, LessonSerializer, EnrollmentSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class EnrollmentModelViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = User
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = User


# class VideoListCreateAPIView(ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#
#
# class VideoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer



# class ChannelListCreateAPIView(ListCreateAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer
#
#
# class ChannelDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer








