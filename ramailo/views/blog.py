from rest_framework.decorators import api_view
from ramailo.models.blog import Post, Comment
from ramailo.serializers.blog_serializer import PostSerializer, CommentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def blog_post(request):
    post = Post.objects.all()

    serializer = PostSerializer(post , many=True)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data , content_type="application/json")

@api_view(['GET'])
def specific_blog(request , post_id):
    post = Post.objects.get(id= post_id)

    serializer = PostSerializer(post)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data , content_type="application/json")


@api_view(['POST'])
def create_blog(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)