from django.db import models

from articleapp.model import Article


class Tag(models.Model):
    name = models.CharField(max_length=100)
    article = models.ManyToManyField(Article, on_delete=models.SET_NULL, null=True)
