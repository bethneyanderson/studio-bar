from django import forms
from django.core.exceptions import ValidationError
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'genre', 'bio', 'social_links']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Artist name'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Genre (e.g., Rock, Jazz, Pop)'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Artist biography (max 500 words)',
                'rows': 4
            }),
            'social_links': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com (optional)'
            })
        }
        labels = {
            'name': 'Artist Name',
            'genre': 'Genre',
            'bio': 'Biography',
            'social_links': 'Social Media Link'
        }

    def clean_bio(self):
        bio = self.cleaned_data.get('bio', '')
        if bio:
            word_count = len(bio.split())
            if word_count > 500:
                raise ValidationError(
                    f'Biography must be 500 words or less. Current word count: {word_count}'
                )
        return bio
