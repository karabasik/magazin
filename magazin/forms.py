from django import forms

class ReviewForm(forms.Form):
    review_text = forms.CharField()
    review_buyer = forms.IntegerField()


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())