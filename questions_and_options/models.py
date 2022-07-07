from urllib import response
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Question(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='questions/images', blank="True")

    def __str__(self):
        return self.description


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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=1000)
