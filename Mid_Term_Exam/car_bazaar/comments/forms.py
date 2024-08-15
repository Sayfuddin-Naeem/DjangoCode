from django import forms
from comments.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'body']
        labels = {
            'body' : 'Comment'
        }