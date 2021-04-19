from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=128)
    photo_movie = models.FileField(upload_to='driver_app/uploads')
    tags = models.ManyToManyField('Tag')
    training = models.ForeignKey('Training', on_delete=models.SET_NULL, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=32)


class Training(models.Model):
    question = models.ManyToManyField('Question', related_name='trainings')


class Question(models.Model):
    content = models.TextField()
    training = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='question_to_training')


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    correct = models.BooleanField(default=False)

