from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Candidate, Question, Option, CandidateResponse, Score
from .serializers import QuestionSerializer, OptionSerializer, CandidateSerializer, ResponseSerializer, ScoreSerializer
# Create your views here.


class QuestionViewset(ModelViewSet):
    queryset = Question.objects.prefetch_related('options').all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class OptionViewset(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminUser]


class CandidateViewset(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        candidate = Candidate.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CandidateSerializer(candidate)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CandidateSerializer(candidate, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class ResponseViewset(ModelViewSet):
    queryset = CandidateResponse.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAdminUser]


class ScoreViewset(ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAdminUser])
    def generate_score(self, request):
        questions = Question.objects.all().values('id')
        candidates = Candidate.objects.all().values('id')
        responses = CandidateResponse.objects.select_related(
            'candidate_id',
            'question_id'
        ).all().values('candidate_response')
        options = Option.objects.select_related('question').filter(answer=1)
        score = 0

        for candidate in candidates:
            cand_id = candidate['id']
            for question in questions:
                ques_id = question['id']
                try:
                    resp = str(responses.get(
                        candidate_id=cand_id,
                        question_id=ques_id
                    )['candidate_response'])
                    answer = str(options.get(question=ques_id))

                    if resp == answer:
                        score += 1
                except CandidateResponse.DoesNotExist:
                    next
            try:
                cand_score = Score.objects.get(candidate=cand_id)
                cand_score.candidate_score = score
                cand_score.save()
            except Score.DoesNotExist:
                Score.objects.create(
                    candidate=Candidate.objects.get(pk=cand_id),
                    candidate_score=score
                )
            score = 0
        score = Score.objects.all()
        serializer = ScoreSerializer(score, many=True)
        return Response(serializer.data)
