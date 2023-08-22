from .models import Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '***Please be mindful as posted comment cannot be changed or deleted without contacting the administration. Inappropriate comments will be removed.***',
        }
