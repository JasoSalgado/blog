"""simple_blog/comments/admin.py"""

# Django modules
from django.contrib import admin

# My modules
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin"""
    list_display = ('id', 'user', 'post', 'comment')