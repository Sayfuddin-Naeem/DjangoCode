from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'
        
class RegistationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text   = None
        self.fields['password1'].help_text  = None
        self.fields['password2'].help_text  = None
        
        self.fields['first_name']   = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        self.fields['last_name']    = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        self.fields['email']        = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))

class ChangeUserDataForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        if 'password' in self.fields:
            del self.fields['password']

class ChangeUserPassForm(PasswordChangeForm):
    def __init__(self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any) -> None:
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].help_text = None
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None