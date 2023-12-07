from .models import Comment
from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['email'].label = 'Email Address'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Write your comment here:',}
