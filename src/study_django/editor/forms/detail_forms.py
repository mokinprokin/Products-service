from editor.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RewiewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
        widget=forms.Select(),
        required=True,
    )
