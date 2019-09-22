from django import forms
from django.contrib.auth import get_user_model
from core.models import Vote, Movie

class VoteForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = get_user_model().objects.all(),
        disabled =True
    )

    movie = forms.ModelChoiceField(
        widget = forms.HiddenInput,
        queryset = Movie.objects.all(),
        disabled = True
    )
    fields = ('value', 'user', 'movie')

    class Meta:
        model = Vote
        fields = ('value', 'user', 'movie')
            