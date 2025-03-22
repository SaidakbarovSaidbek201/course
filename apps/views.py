from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import User, Video, Channel, Video, Comment, CommentLike, VideoLike
from .serializers import UserSerializer, VideoSerializer, ChannelSerializer, CommentSerializer, CommentLikeSerializer, VideoLikeSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet


# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = User
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = User

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class VideoListCreateAPIView(ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#
#
# class VideoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

class VideoModelViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


# class ChannelListCreateAPIView(ListCreateAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer
#
#
# class ChannelDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer


class ChannelModelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class VideoLikeModelViewSet(ModelViewSet):
    queryset = VideoLike.objects.all()
    serializer_class = VideoLikeSerializer

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentLikelModelViewSet(ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer






