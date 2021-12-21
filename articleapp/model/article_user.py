from django.db import models


from articleapp.model import Article


class ArticleUsers(models.Model):
    user_info = models.CharField
    article = models.ManyToManyField(Article, on_delete=models.SET_NULL)

