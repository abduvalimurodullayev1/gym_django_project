from django import forms
from django.forms import ModelForm

from app.models import ContactMessage


class ContactForm(ModelForm):

    class Meta:
        model = ContactMessage
        exclude = ()



