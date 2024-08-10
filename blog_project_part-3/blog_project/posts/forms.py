from django import forms
from posts.models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        # widgets = {
        #     'category' : forms.CheckboxSelectMultiple()
        # }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']
        