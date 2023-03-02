from datetime import datetime
from django import forms
from .models import Post, RentRequest

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        labels = {
            'title': 'Tittel:',
            'text': 'Beskrivelse:',
            'image': 'Last opp bilde:'
        }

class RentRequestForm(forms.ModelForm):
    class Meta:
        model = RentRequest
        fields = ('start_date', 'end_date', 'description')
        labels = {
            'start_date': 'Fra dato:',
            'end_date': 'Til dato:',
            'description': 'Beskrivelse:'
        }        
        