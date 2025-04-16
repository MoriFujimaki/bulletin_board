from django.db import models
from django.contrib.auth.models import User
class Thread(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # ← ここ変更
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    delete_password = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return f'{self.author.username if self.author else "匿名"}: {self.content[:20]}'