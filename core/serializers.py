from rest_framework import serializers
from .models import Question, Option, Candidate, CandidateResponse, Score


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'id',
            'question',
            'description',
        ]


class SimpleOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'id',
            'description',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = SimpleOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'description',
            'image',
            'options'
        ]


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'id',
            'user_id',
            'phone_number',
            'candidate_picture',
        ]


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateResponse
        fields = [
            'question_id',
            'candidate_id',
            'candidate_response'
        ]

    def save(self, **kwargs):
        question_id = self.validated_data['question_id']
        candidate_id = self.validated_data['candidate_id']
        candidate_response = self.validated_data['candidate_response']

        try:
            response = CandidateResponse.objects.get(
                question_id=question_id, candidate_id=candidate_id)
            response.candidate_response = candidate_response
            response.save()
            self.instance = response
        except CandidateResponse.DoesNotExist:
            self.instance = CandidateResponse.objects.create(
                **self.validated_data
            )

        return self.instance


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['candidate', 'candidate_score']
