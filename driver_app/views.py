from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from driver_app.models import Advice, Answer, Question, Training, Tag
from driver_app.serializers import AdviceSerializer, AnswerSerializer, QuestionSerializer, TrainingSerializer, \
    TagSerializer


class AdviceAPIView(generics.ListCreateAPIView):
    queryset = Advice.objects.all().order_by('?')
    serializer_class = AdviceSerializer


class AdviceDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AnswerAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TrainingAPIView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TrainingDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
