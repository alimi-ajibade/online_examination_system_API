from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Question, Option
from .serializers import QuestionSerializer, OptionSerializer
# Create your views here.


class QuestionViewset(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionViewset(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
