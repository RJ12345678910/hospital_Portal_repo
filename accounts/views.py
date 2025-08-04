from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
import random
from .forms import DoctorVerificationForm
from django.contrib.auth import get_user_model
from .models import DoctorVerification

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = SignupForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			if user.user_type == 'doctor':
				return redirect('verify_doctor', user_id=user.id)
			else:
				return redirect('home')
	else:
		form = SignupForm()
	
	return render(request, 'signup.html', {'form': form})

User = get_user_model()
def verify_doctor(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = DoctorVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.user = user
            verification.save()
            return redirect('login')
    else:
        form = DoctorVerificationForm()
    return render(request, 'accounts/verify.html', {'form': form, 'user': user})


def login_view(request):
    user_type = request.GET.get('user_type', None)  # Get type from URL

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = AuthenticationForm()
    
    facts = [
        "Drink water",
        "Wash hands regularly",
        "Exercise daily",
        "Eat more greens",
        "Get enough sleep",
        "Limit sugar intake",
        "Regular checkups save lives",
        "Take stairs instead of elevators"
    ]

    context = {
    	'form': form,
        'user_type': user_type,
        'random_fact': random.choice(facts) if user_type == 'patient' else None,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def patient_dashboard(request):
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'profile_pic': user.profile_pic,
        'address_line1': user.address_line1,
        'city': user.city,
        'state': user.state,
        'pincode': user.pincode,
    }
    return render(request, 'accounts/patient_dashboard.html', context)


def doctor_dashboard_unverified(request):
	return render(request, 'accounts/doctor_dashboard_unverified', {'user': user})
@login_required
def doctor_dashboard(request):
    user = request.user
    verification = get_object_or_404(DoctorVerification, user=user)
    
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'profile_pic': user.profile_pic,
        'address_line1': user.address_line1,
        'city': user.city,
        'state': user.state,
        'pincode': user.pincode,
        'medical_license_number': verification.medical_license_number,
        'college_name': verification.college_name,
        'degree': verification.degree,
        'phone_number1': verification.phone_number1,
        'phone_number2': verification.phone_number2,
        'degree_photo': verification.degree_photo,
        'govt_id_photo': verification.govt_id_photo,
        'verified': verification.verified,
    }
    return render(request, 'accounts/doctor_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')  

def home_view(request):
	return render(request, 'accounts/home.html')