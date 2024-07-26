from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Length must be within 50 character', 
            widget= forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1', 'placeholder' : 'Enter Your Name' }))
    # file = forms.FileField()
    
    email = forms.CharField(label='User Email', widget= forms.EmailInput)
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
    meal = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)


# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at list 10 charecters")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at list 10 charecters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")

def len_check(text):
    if len(text) < 10:
        raise forms.ValidationError('Text lenght at least 10 charecters')

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 charecters'), 
            validators.MaxLengthValidator(35, message='Enter a name with at most 35 charecters')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator])
    age = forms.IntegerField(validators=[validators.MinValueValidator(23, message='Age must be at least 23'), validators.MaxValueValidator(34, message='Age must be maximum 34')])
    

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data['name']
        valPassword = self.cleaned_data['password']
        valConPassword = self.cleaned_data['confirm_password']
        
        if len(valName) < 10:
            raise forms.ValidationError("Enter a name with at list 10 charecters")
        if valPassword != valConPassword:
            raise forms.ValidationError("Password dosen't match !")
    
    