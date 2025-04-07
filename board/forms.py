from django import forms
from .models import Post
from .models import Thread
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content'] 
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="検索")
