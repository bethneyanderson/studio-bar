from django import forms
from .models import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = [
            'story_title', 'story_lead', 'story_content',
            'mission_title', 'mission_content',
            'space_title', 'space_content', 
            'programming_title', 'programming_content',
            'community_title', 'community_content',
            'address', 'opening_hours', 'email'
        ]
        
        widgets = {
            'story_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section title'}),
            'story_lead': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Lead paragraph...'}),
            'story_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Additional content...'}),
            'mission_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section title'}),
            'mission_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mission content...'}),
            'space_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section title'}),
            'space_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Space description...'}),
            'programming_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section title'}),
            'programming_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Programming content...'}),
            'community_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section title'}),
            'community_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Community content...'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Venue address...'}),
            'opening_hours': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Opening hours...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@email.com'}),
        }
