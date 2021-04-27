import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from driver_app.models import Advice, Answer, Question, Training, Tag
from driver_app.serializers import AdviceSerializer, AnswerSerializer, QuestionSerializer, TrainingSerializer, \
    TagSerializer, UserSerializer


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckTraining(APIView):
    @csrf_exempt  # TEMPORARY
    def post(self, request):
        print(request.data)
        t = Training.objects.get(pk=request.data['training-id'])
        questions = t.question_to_training.all()
        correct_answers = []
        for q in questions:
            print(q.answers.all())
        return Response({}, status=200)
