from django.contrib.auth.models import User
from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=128)
    photo_movie = models.FileField(upload_to='driver_app/uploads', blank=True)
    tags = models.ManyToManyField('Tag')
    training = models.ForeignKey('Training', on_delete=models.SET_NULL, null=True, blank=True)
    users_passed_advice = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=32)


class Training(models.Model):
    pass


class Question(models.Model):
    content = models.TextField()
    training = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='question_to_training')

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers', blank=True)
    content = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

