from django.contrib import admin

from ramailo.models.feedback import Feedback
from ramailo.models.notification import FCMDevice
from ramailo.models.user import User
from .models.blog import Post, Comment, Category, PostImage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'idx', 'mobile', 'name', 'position', 'created_at']
    search_fields = ['name', 'mobile']
    list_filter = ['is_approved', 'is_email_verified', 'is_kyc_verified']


admin.site.register(FCMDevice)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'is_published')
    list_filter = ('is_published', 'created_date', 'categories')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'url')
