from django import forms
from django.forms import ModelForm

from .models import Rant

class RantForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type here...'})) 
    poster = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Optional: default as Anonymous'}))

    class Meta:
        model = Rant
        fields = "__all__"
