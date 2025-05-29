from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('tech', 'Technology'),
        ('others', 'Others'),
    ]
    
    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.get_name_display()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

class PostImage(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='image')
    url = models.URLField()
    
    def __str__(self):
        return f'Image for {self.post.title}' 