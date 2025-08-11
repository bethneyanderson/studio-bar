from django import forms
from django.core.exceptions import ValidationError
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description', 'artist', 'image', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Event Description (max 500 words)'
            }),
            'artist': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00'
            })
        }
        labels = {
            'title': 'Event Title',
            'date': 'Date and Time',
            'description': 'Description',
            'artist': 'Artist',
            'image': 'Image',
            'price': 'Ticket Price ($)'
        }

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description:
            word_count = len(description.split())
            if word_count > 500:
                raise ValidationError(
                    f'Description must be 500 words or less. Current word count: {word_count}'
                )
        return description
