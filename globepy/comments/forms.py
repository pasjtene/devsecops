from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 3,'placeholder': 'Your comment...'}),
            
        }

