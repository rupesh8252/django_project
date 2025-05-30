from rest_framework import serializers
from django.contrib.auth import get_user_model
from ramailo.models.blog import Post, Comment, Category, PostImage

User = get_user_model()

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    is_published = serializers.BooleanField(default=False)
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(), required=False)


class CommentSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    content = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class PostImageSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    url = serializers.URLField()
    