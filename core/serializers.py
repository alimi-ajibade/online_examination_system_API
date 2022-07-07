from requests import options
from rest_framework import serializers
from . import models


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = [
            'id',
            'question',
            'description',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
            'id',
            'description',
            'image',
        ]

        opts = serializers.SerializerMethodField(
            method_name='option_list'
        )

    # def option_list(self, question: models.Question):
    #     return list(models.Option.objects.filter(question=question.id))
