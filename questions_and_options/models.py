from email.mime import image
from django.db import models

# Create your models here.


class Questions(models.Model):
    description = models.CharField(max_length=100000000000)
    image = models.ImageField(upload_to='questions/images')


class Options(models.Model):
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name='question',
    )
    description = models.CharField(max_length=1000000000)
    answer = models.BooleanField(default=False)
