from django import forms
from .models import NoteModel

class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'content']