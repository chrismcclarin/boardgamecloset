from django.forms import ModelForm
from .models import GameTime

class GameTimeForm(ModelForm):
    class Meta:
        model = GameTime
        fields = ('date', 'location', 'timeplayed')