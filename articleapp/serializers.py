from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'creation_date', 'category_id', 'article_status']
