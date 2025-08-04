#forms.py...
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import DoctorVerification

class SignupForm(UserCreationForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

	class Meta:
		model = CustomUser
		fields = [
            'first_name',
            'last_name',
            'profile_pic',
            'username',
            'email',
            'password1',
            'password2',
            'address_line1',
            'city',
            'state',
            'pincode',
            'user_type',
		]

class DoctorVerificationForm(forms.ModelForm):
    class Meta:
        model = DoctorVerification
        exclude = ['user', 'verified']
