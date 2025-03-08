from django.db import models
from patient.models import Patient
from patient.models import Doctor




class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="prescriptions")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_prescriptions")
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    instructions = models.TextField()
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.first_name} by Dr. {self.doctor.name}"



