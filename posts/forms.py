from datetime import datetime
from django import forms
from .models import *

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        labels = {
            'title': 'Tittel:',
            'text': 'Beskrivelse:',
            'image': 'Last opp bilde:'
        }

class RateRentalForm(forms.Form):
    user_rating = forms.IntegerField(label='Vurdering av utleier:', min_value=1, max_value=5)
    post_rating = forms.IntegerField(label='Vurdering av utleid redskap:', min_value=1, max_value=5)
    
class RentRequestForm(forms.ModelForm):
    class Meta:
        model = RentRequest
        fields = ('start_date', 'end_date', 'description')
        labels = {
            'start_date': 'Fra dato:',
            'end_date': 'Til dato:',
            'description': 'Beskrivelse:'
        }        
        
