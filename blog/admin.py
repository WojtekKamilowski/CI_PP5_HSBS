from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Blog posts admin
    """
    list_display = ('post_title', 'slug', 'created_on')
    search_fields = ['post_title', 'content']
    list_filter = ('created_on',)
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Blog posts comments admin
    """
    list_display = ('username', 'body', 'post', 'created_on')
    list_filter = ('created_on', 'username',)
    search_fields = ('username', 'email', 'body')
