#urls.py...
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_view, name='home'),
	path('signup/', views.signup_view, name='signup'),
	path('verify-doctor/<int:user_id>/', views.verify_doctor, name='verify_doctor'),
	path('doctor_dashboard_unverified/', views.doctor_dashboard_unverified, name="doctor_dashboard_unverified"),
	path('login/', views.login_view, name='login'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/', views.logout_view, name='logout'),

]