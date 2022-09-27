from django import forms

from .models import BlogPostComment


class BlogPostCommentForm(forms.ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ("name", "comment")
