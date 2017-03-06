from django import forms

class SendEmailForm(forms.Form):
    subtitle = forms.CharField(max_length=100)
    content = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'size':500
                }
            )
        )
    recipient = forms.CharField(max_length=100)
