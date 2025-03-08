from django.urls import reverse

from .forms import PatientRegistrationForm, AppointmentBookingForm, MedicalHistoryForm, DoctorForm

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from .models import Billing, Doctor
from .forms import BillingForm

import stripe




def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_appointment')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/register.html', {'form': form})




def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'patient/doctor_list.html', {'doctors': doctors})



def book_appointment(request):
    form = AppointmentBookingForm()  # Ensure form is defined before any condition

    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page

    return render(request, 'patient/appointment_booking.html', {'form': form})


def appointment_success(request):
    return render(request, 'patient/appointment_success.html')

def add_medical_history(request):
    form = MedicalHistoryForm()

    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = MedicalHistoryForm()

    return render(request, 'patient/medical_history.html', {'form': form})





# Set up Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_invoice(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            bill = form.save()
            return redirect('stripe_payment', bill.invoice_id)  # Redirect to payment page
    else:
        form = BillingForm()

    return render(request, 'patient/billing.html', {'form': form})

def stripe_payment(request, invoice_id):
    bill = get_object_or_404(Billing, invoice_id=invoice_id)
    stripe_checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': f'Invoice {bill.invoice_id}',
                },
                'unit_amount': int(bill.amount * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/payment-success/'),
        cancel_url=request.build_absolute_uri('/billing/'),
    )

    return render(request, 'stripe_payment.html', {
        'checkout_session_id': stripe_checkout_session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'bill': bill,
    })

def payment_success(request):
    return render(request, 'patient/payment_success.html')







