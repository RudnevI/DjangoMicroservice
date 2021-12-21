from .models import Article, Category, Tag, ArticleUser
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        category = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field="name"
        )
        fields = ['title', 'content', 'category', 'article_status']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['parent_id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'article']


class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleUser
        fields = ['user_info', 'article']
