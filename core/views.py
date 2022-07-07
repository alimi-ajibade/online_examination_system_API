from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Candidate, Question, Option
from .serializers import QuestionSerializer, OptionSerializer, CandidateSerializer
# Create your views here.


class QuestionViewset(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionViewset(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class CandidateViewset(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
