from django.urls import path


from .views import user_list, user_create, user_update, user_delete, login_view, logout_view, update_doctor, \
    delete_doctor, add_doctor, delete_appointment, home
from .views import facility_list, facility_create, facility_update, facility_delete
from .views import appointment_list, appointment_update,admin_patient_list,admin_update_patient, admin_delete_patient


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', user_list, name='user_list'),
    path('users/add/', user_create, name='user_create'),
    path('users/edit/<int:user_id>/', user_update, name='user_update'),
    path('users/delete/<int:user_id>/', user_delete, name='user_delete'),

    path('patients/', admin_patient_list, name='admin_patient_list'),
    path('patients/update/<int:patient_id>/', admin_update_patient, name='admin_update_patient'),
    path('patients/delete/<int:patient_id>/', admin_delete_patient, name='admin_delete_patient'),

    path('facilities/', facility_list, name='facility_list'),
    path('facilities/add/', facility_create, name='facility_create'),
    path('facilities/edit/<int:facility_id>/', facility_update, name='facility_update'),
    path('facilities/delete/<int:facility_id>/', facility_delete, name='facility_delete'),

    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/edit/<int:appointment_id>/', appointment_update, name='appointment_update'),
    path('appointments/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),

    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/update/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('doctors/delete/<int:doctor_id>/', delete_doctor, name='delete_doctor'),

    path('', home, name='home')
]


