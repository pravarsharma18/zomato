from django import forms

class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['email','password']

    