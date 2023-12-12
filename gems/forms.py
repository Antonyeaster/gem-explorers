from .models import Comment
from django import forms
from allauth.account.forms import SignupForm
from django.core.validators import MaxLengthValidator

""" https://stackoverflow.com/questions/50548685/how-to-add-max-length-to-allauth-username"""


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['email'].label = 'Email Address'
        self.fields['username'].validators += [MaxLengthValidator(
            20, "Username should be 20 characters or less")]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Write your comment below:', }
