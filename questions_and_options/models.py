from django.db import models

# Create your models here.


class Question(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='questions/images', blank="True")


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
