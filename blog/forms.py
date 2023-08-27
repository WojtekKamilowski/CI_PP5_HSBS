from .models import Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '***Please be mindful as posted comment cannot be changed or deleted. Inappropriate comments are to be removed by the administration.***',
        }
