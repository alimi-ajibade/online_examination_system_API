from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Candidate, Question, Option, Response
from .serializers import QuestionSerializer, OptionSerializer, CandidateSerializer, ResponseSerializer
# Create your views here.


class QuestionViewset(ModelViewSet):
    queryset = Question.objects.prefetch_related('options').all()
    serializer_class = QuestionSerializer


class OptionViewset(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class CandidateViewset(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ResponseViewset(ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    # def get_serializer_context(self):
    #     return {
    #         'question_id': self.kwargs['question_id'],
    #         'candidate_id': self.kwargs['candidate_id'],
    #     }
