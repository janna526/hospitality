
from django.db import models


import uuid



class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name





class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")  # ✅ Ensure this exists

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending')

    def __str__(self):
        return f"{self.patient.first_name} - {self.appointment_date} at {self.appointment_time}"


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField(blank=True, null=True)
    treatment_history = models.TextField()

    def __str__(self):
        return f"Medical History of {self.patient.first_name} {self.patient.last_name}"




class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.patient.first_name}"










