from django import forms

class NewsletterSignUpForm(forms.Form):
    email = forms.EmailField(label="Your email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
