from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('nickname', 'name', 'surname', 'gender', 'age', 'phone_number', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }