from django import forms
from django.forms import ModelForm

from .models import Rant

class RantForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type here...'}))

    class Meta:
        model = Rant
        fields = "__all__"
