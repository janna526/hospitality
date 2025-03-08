from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

from patient.forms import DoctorForm, PatientRegistrationForm, AppointmentBookingForm
from patient.models import Patient, Doctor,Appointment
from .forms import UserRegistrationForm, UserUpdateForm , Facility, FacilityForm

from .forms import PatientUpdateForm

User = get_user_model()



def is_admin_logged_in(request):
    return request.session.get('is_logged_in', False)  # Session-based check


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            request.session['is_logged_in'] = True
            return redirect('admin_patient_list')
        else:
            return render(request, 'admin/login.html', {'error': 'Invalid credentials or not an admin'})

    return render(request, 'admin/login.html')


def logout_view(request):
    logout(request)
    request.session.flush()  # Clear session
    return redirect('login')


def user_list(request):

    users = User.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})


def user_create(request):
    if not is_admin_logged_in(request):
        return redirect('login')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'admin/user_form.html', {'form': form})


def user_update(request, user_id):
    if not is_admin_logged_in(request):
        return redirect('login')

    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'admin/user_form.html', {'form': form})


def user_delete(request, user_id):
    if not is_admin_logged_in(request):
        return redirect('login')

    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'admin/user_confirm_delete.html', {'user': user})




def admin_patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'admin/patient_list.html', {'patients': patients})


def admin_update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('admin_patient_list')  # Redirect back to patient list
    else:
        form = PatientUpdateForm(instance=patient)

    return render(request, 'admin/patient_update.html', {'form': form, 'patient': patient})


def admin_delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('admin_patient_list')

    return render(request, 'admin/patient_confirm_delete.html', {'patient': patient})



def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'admin/facility_list.html', {'facilities': facilities})

def facility_create(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()

    return render(request, 'admin/facility_form.html', {'form': form})

def facility_update(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)

    return render(request, 'admin/facility_form.html', {'form': form})

def facility_delete(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        facility.delete()
        return redirect('facility_list')

    return render(request, 'admin/facility_confirm_delete.html', {'facility': facility})




def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin/appointment_list.html', {'appointments': appointments})



def appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentBookingForm(instance=appointment)

    return render(request, 'admin/appointment_form.html', {'form': form})



def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')  # ✅ Redirect after deletion

    return render(request, 'admin/appointment_confirm_delete.html', {'appointment': appointment})


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()

    return render(request, 'patient/doctor_form.html', {'form': form, 'title': 'Add Doctor'})



def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'patient/doctor_form.html', {'form': form, 'title': 'Update Doctor'})


def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')

    return render(request, 'patient/doctor_confirm_delete.html', {'doctor': doctor})


def home(request):
    return render(request,'admin/home.html')