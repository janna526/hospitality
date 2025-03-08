from django.urls import path
from .views import patient_register, payment_success, doctor_list
from .views import book_appointment,add_medical_history,create_invoice,stripe_payment,appointment_success



urlpatterns = [
    path('register/', patient_register, name='patient_register'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('appointment-success/', appointment_success, name='appointment_success'),
    path('medical-history/', add_medical_history, name='medical_history'),
    path('billing/', create_invoice, name='billing'),
    path('stripe-payment/<uuid:invoice_id>/', stripe_payment, name='stripe_payment'),
    path('payment-success/', payment_success, name='payment_success'),




]






