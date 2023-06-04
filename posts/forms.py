from django import forms
from django.forms import ModelForm

from posts.models import Post, Comment


class PostCreateForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название поста...',
    }))
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Текст поста...',
    }))
    img = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
    }), required=False)

    class Meta:
        model = Post
        fields = ('img', 'title', 'text')


class CommentForm(ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш комментарий...',
    }))

    class Meta:
        model = Comment
        fields = ('text',)