from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes_question')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=0)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
