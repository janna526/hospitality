from django import forms


from . models import Patient,Doctor,Appointment,MedicalHistory,Billing




class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone', 'dob', 'address', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),

        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'email', 'phone']



class AppointmentBookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time','status']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'diagnosis', 'medications', 'allergies', 'treatment_history']





class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'amount']



