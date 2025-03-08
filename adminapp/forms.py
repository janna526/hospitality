from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Facility
from patient.models import Patient




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone', 'dob', 'address', 'gender']



class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'departments']






