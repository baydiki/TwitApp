from django import forms
from django.forms import ModelForm
from twitter_app.models import Twit
class TweetForm(forms.Form):
    content = forms.CharField(label='Tweet Content', max_length=280, widget=forms.Textarea(attrs={'rows': 3,'class': 'tweetcontent'}))
    nickname = forms.CharField(label='Nickname', max_length=50)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

# Modelimizi oluşturduk
class AddTweetModelForm(ModelForm):
    class Meta:
        model = Twit
        fields = ['nickname', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3,'class': 'tweetcontent'}),
            'nickname': forms.TextInput(attrs={'class': 'nicknameinput'}),
        }
