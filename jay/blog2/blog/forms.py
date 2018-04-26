from django import forms
from .models import Post,Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        eclude = ('post','author',)
        fields = ('text',)