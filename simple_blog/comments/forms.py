"""simple_blog/comments/forms.py"""

# Django modules
from django import forms

# My modules
from comments.models import Comment
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):
    """Post model form"""

    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Form settings"""

        model = Comment
        fields = ('user', 'profile', 'post', 'comment')