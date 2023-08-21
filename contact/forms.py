from django import forms
from .models import Contact


# The contact form for the user to send a message to the business


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
