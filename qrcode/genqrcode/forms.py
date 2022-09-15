from django import forms
from .models import QRCode
from django.forms import ModelForm

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = "__all__"
