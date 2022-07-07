from django.contrib import admin
from django.db.models import Q
from . import models

# Register your models here.


class OptionInline(admin.TabularInline):
    model = models.Option


@admin.register(models.Question)
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
        queryset = list(models.Option.objects.filter(question_id=question.id))
        return queryset

    def answer(self, question):
        return list(models.Option.objects.filter(Q(question_id=question.id) & Q(answer=1)))


@ admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'description',
        'answer',
    ]
    autocomplete_fields = ['question']
    search_fields = ['description']


@admin.register(models.Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        'candidate_id',
        'question_id',
        'response'
    ]


@admin.register(models.Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'middle_name',
        'phone_number',
        'email'
    ]
    list_select_related = ['user']
