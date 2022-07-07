from django.db import models

# Create your models here.


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    # email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Question(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='questions/images', blank="True")

    def __str__(self):
        return self.description[:50]


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='question',
    )
    description = models.CharField(max_length=1000)
    answer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description


class Response(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=1000)
