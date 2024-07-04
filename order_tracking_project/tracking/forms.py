from django import forms
from .models import TrackedOrder

class TrackedOrderForm(forms.ModelForm):
    class Meta:
        model = TrackedOrder
        fields = ['order', 'status']
