from django import forms
from django.utils.html import strip_tags
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_number',
            'vehicle_type',
            'vehicle_model',
            'vehicle_description',
        ]

    def clean_vehicle_description(self):
        data = self.cleaned_data.get('vehicle_description', '')
        # Basic XSS handling: remove any HTML tags
        cleaned = strip_tags(data)
        return cleaned

    def clean_vehicle_number(self):
        data = self.cleaned_data.get('vehicle_number', '')
        # Basic XSS handling: remove any HTML tags
        cleaned = strip_tags(data)
        return cleaned

    def clean_vehicle_model(self):
        data = self.cleaned_data.get('vehicle_model', '')
        # Basic XSS handling: remove any HTML tags
        cleaned = strip_tags(data)
        return cleaned