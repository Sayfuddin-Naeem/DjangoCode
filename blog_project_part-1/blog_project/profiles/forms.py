from django import forms
from profiles.models import Profiles

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
        