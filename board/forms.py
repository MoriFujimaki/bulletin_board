from django import forms
from .models import Post
from .models import Thread
from django import forms
class PostForm(forms.ModelForm):
      delete_password = forms.CharField(widget=forms.PasswordInput(), required=False, label="削除用パスワード")
      class Meta:
        model = Post
        fields = ['content', 'delete_password']
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="検索")
