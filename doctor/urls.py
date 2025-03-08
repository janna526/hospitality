from django.urls import path
from .views import patient_list, patient_detail, add_medical_record, doctor_appointments, update_appointment
from .views import prescription_list, add_prescription, edit_prescription, delete_prescription



urlpatterns = [
    path('patients/', patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/add-medical-record/', add_medical_record, name='add_medical_record'),


    path('appointments/<int:doctor_id>/', doctor_appointments, name='doctor_appointments'),
    path('appointments/update/<int:appointment_id>/', update_appointment, name='update_appointment'),

    path('prescriptions/<int:doctor_id>/', prescription_list, name='prescription_list'),
    path('prescriptions/add/<int:patient_id>/<int:doctor_id>/', add_prescription, name='add_prescription'),
    path('prescriptions/edit/<int:prescription_id>/', edit_prescription, name='edit_prescription'),
    path('prescriptions/delete/<int:prescription_id>/', delete_prescription, name='delete_prescription')
]



