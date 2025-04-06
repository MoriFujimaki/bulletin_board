from django.contrib import admin
from .models import Thread, Post
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'author', 'created_at')
    search_fields = ('content', 'author__username')
    list_filter = ('created_at',)