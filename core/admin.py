from django.contrib import admin
from django.db.models import Q
from .models import Question, Option, CandidateResponse, Candidate, Score

# Register your models here.


class OptionInline(admin.TabularInline):
    model = Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'image',
        'options',
        'answer'
    ]
    search_fields = ['description']
    inlines = [OptionInline]

    def options(self, question):
        queryset = list(Option.objects.filter(question_id=question.id))
        return queryset

    def answer(self, question):
        return list(Option.objects.filter(Q(question_id=question.id) & Q(answer=1)))


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'description',
        'answer',
    ]
    autocomplete_fields = ['question']
    search_fields = ['description']


@admin.register(CandidateResponse)
class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        'candidate_id',
        'question_id',
        'candidate_response'
    ]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'first_name',
        'last_name',
        'middle_name',
        'phone_number',
        'email',
        'candidate_picture'
    ]
    list_select_related = ['user']


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = [
        'candidate',
        'candidate_score',
    ]
