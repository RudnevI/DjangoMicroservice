from .models import Article, Category, Tag, ArticleUser
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['parent_id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ['title', 'content', 'category', 'article_status']
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'article']


class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleUser
        fields = ['user_info', 'article']
