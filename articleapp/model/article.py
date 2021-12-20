from django.db import models
from django.utils import timezone

from articleapp.model.category import Category


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000)
    creation_datetime = models.DateTimeField(default=timezone.localtime(timezone.now()))
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL)
    HIDDEN = 'HIDDEN'
    PUBLIC = 'PUBLIC'
    ARTICLE_STATUS_CHOICES = [
        (HIDDEN, 'Hidden'),
        (PUBLIC, 'Public')
    ]
    article_status = models.CharField(
        max_length=30,
        choices=ARTICLE_STATUS_CHOICES,
        default=PUBLIC
    )
