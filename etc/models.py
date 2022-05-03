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
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='question_likes')
    added_at = models.DateTimeField(auto_now_add=True)

    def get_answers(self):
        return Answer.objects.filter(question_id=self.id)

class Answer(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)