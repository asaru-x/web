from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    def __init__(self):
        self.title = models.CharField(max_length=64)
        self.text = models.TextField()
        self.added_at = models.DateTimeField(auto_now_add=True)
        self.likes = models.ManyToManyField(User, related_name='likes_question')
        self.author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        self.rating = models.IntegerField(default=0)

class Answer(models.Model):
    def __init__(self):
        self.text = models.TextField()
        self.added_at = models.DateTimeField(auto_now_add=True)
        self.author = models.CharField(max_length=64)
        self.question = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

