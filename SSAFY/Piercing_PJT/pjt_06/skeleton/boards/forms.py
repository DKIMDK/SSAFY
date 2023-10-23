from django import forms
from .models import Board, Comment# , Cocomment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

# class CocommentForm(forms.ModelForm):
#     class Meta:
#         model = Cocomment
#         fields = ('content', )