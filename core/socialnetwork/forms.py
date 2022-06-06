from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'image', 'status']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'placeholder': 'Enter the title','class':'form-control'}
        self.fields['author'].widget.attrs = {'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Write your post here...', 'class':'form-control', 'rows':'5'}
        self.fields['image'].widget.attrs = {'class':'form-control'}
        self.fields['status'].widget.attrs = {'class':'form-control'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Enter name','class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Enter email', 'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...', 'class':'form-control', 'rows':'5'}
