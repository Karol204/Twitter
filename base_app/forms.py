from django import forms


class addTweetForm(forms.Form):

    content = forms.CharField(max_length=250)