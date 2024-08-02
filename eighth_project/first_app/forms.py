from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    # password1 = forms.CharField(
    #     label="Password",
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     help_text=None,
    # )
    # password2 = forms.CharField(
    #     label="Password confirmation",
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    #     help_text=None,
    # )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # help_texts = {
        #     'username' : None,
        # }
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.help_text = None
    #         field.widget.attrs.update({'class': 'form-control'})  # Add Bootstrap class
    
class MyPasswordChangeForm(PasswordChangeForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = None

class MySetPasswordForm(SetPasswordForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = None

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = None    