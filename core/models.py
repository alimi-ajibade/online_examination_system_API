from distutils.command.upload import upload
from django.db import models
from django.conf import settings

# Create your models here.


class Candidate(models.Model):
    candidate_picture = models.ImageField(
        upload_to='candidate/images', blank=True, null=True)
    middle_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def user_id(self):
        return self.user.id

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Question(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='questions/images', blank="True")

    def __str__(self):
        return self.description[:50]


class CandidateResponse(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    candidate_response = models.CharField(max_length=1000)


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )
    description = models.CharField(max_length=1000)
    answer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description


class Score(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    candidate_score = models.PositiveIntegerField()

    def user_id(self):
        return self.candidate.user.id
