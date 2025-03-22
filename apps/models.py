from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# User, Channel, Video, Comment, Like, Dislike

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.URLField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def __str__(self):
        return self.name

    def count_subscribers(self):
        return self.subscribers.count()


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    video_url = models.URLField(null=True)
    video_file = models.FileField(upload_to='videos/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"


STATUS = (
    ('like', 'like'),
    ('dislike', 'dislike')
)


class VideoLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment.text}"
