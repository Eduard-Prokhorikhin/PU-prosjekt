from datetime import datetime
from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image')
        labels = {
            'title': 'Tittel:',
            'category': 'Kategori',
            'text': 'Beskrivelse:',
            'image': 'Last opp bilde:'
        }
