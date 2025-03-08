from django import forms
from .models import  Prescription
from patient.models import Appointment


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']




class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medication_name', 'dosage', 'instructions']


