from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)  

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus':True, 'id':'user_name', 'class':'form-control form-control-lg', 'placeholder':''}),
    )

    password = forms.CharField(   
        strip=False,
        widget=forms.PasswordInput(attrs={'id':'user_password', 'class':'form-control form-control-lg', 'placeholder':''}),
    )