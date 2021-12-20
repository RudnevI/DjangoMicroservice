from .models import Article, Category
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category_id', 'article_status']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['parent_id', 'name']
