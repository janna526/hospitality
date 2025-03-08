from django.shortcuts import render, get_object_or_404, redirect
from patient.models import MedicalHistory, Patient
from patient.forms import MedicalHistoryForm, Appointment,AppointmentBookingForm
from .models import Prescription
from .forms import PrescriptionForm


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'doctor/patient_list.html', {'patients': patients})

# View patient details
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    medical_records = MedicalHistory.objects.filter(patient=patient)
    return render(request, 'doctor/patient_detail.html', {'patient': patient, 'medical_records': medical_records})

# Add or update medical record
def add_medical_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = patient
            medical_record.save()
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = MedicalHistoryForm()

    return render(request, 'doctor/medical_record_form.html', {'form': form, 'patient': patient})








def doctor_appointments(request, doctor_id):
    appointments = Appointment.objects.filter(doctor_id=doctor_id).order_by('appointment_date', 'appointment_time')
    return render(request, 'doctor/appointment_list.html', {'appointments': appointments})

# Update appointment status
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor_appointments', doctor_id=appointment.doctor.id)
    else:
        form = AppointmentBookingForm(instance=appointment)

    return render(request, 'doctor/appointment_form.html', {'form': form, 'appointment': appointment})





def prescription_list(request, doctor_id):
    prescriptions = Prescription.objects.filter(doctor_id=doctor_id).order_by('-prescribed_at')
    return render(request, 'doctor/prescription_list.html', {'prescriptions': prescriptions})

# Add a new prescription
def add_prescription(request, patient_id, doctor_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = patient
            prescription.doctor_id = doctor_id
            prescription.save()
            return redirect('prescription_list', doctor_id=doctor_id)
    else:
        form = PrescriptionForm()

    return render(request, 'doctor/prescription_form.html', {'form': form, 'patient': patient})


def edit_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list', doctor_id=prescription.doctor.id)
    else:
        form = PrescriptionForm(instance=prescription)

    return render(request, 'doctor/prescription_form.html', {'form': form})

# Delete a prescription
def delete_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    if request.method == 'POST':
        doctor_id = prescription.doctor.id
        prescription.delete()
        return redirect('prescription_list', doctor_id=doctor_id)

    return render(request, 'doctor/prescription_confirm_delete.html', {'prescription': prescription})
