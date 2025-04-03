# from .views import UserListCreateAPIView, UserDetailAPIView, VideoListCreateAPIView, VideoDetailAPIView, ChannelListCreateAPIView, ChannelDetailAPIView
from django.urls import path, include
from .views import UserModelViewSet, CourseModelViewSet, LessonModelViewSet, EnrollmentModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserModelViewSet)  # Avtomatik CRUD marshrutlar
router.register(r'courses', CourseModelViewSet)
router.register(r'lessons', LessonModelViewSet)
router.register(r'enrollment', EnrollmentModelViewSet)


urlpatterns = [
    # path('users/', UserListCreateAPIView.as_view(), name='user_list'),
    # path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    # path('videos/', VideoListCreateAPIView.as_view(), name='video_list'),
    # path('videos/<int:pk>/', VideoDetailAPIView.as_view(), name='video_detail'),
    # path('channels/', ChannelListCreateAPIView.as_view(), name='channel_list'),
    # path('channels/<int:pk>/', ChannelDetailAPIView.as_view(), name='channel_detail'),
    path('', include(router.urls))
]
