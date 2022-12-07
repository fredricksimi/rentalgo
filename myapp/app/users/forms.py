from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email')

class ProfileFirstUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'address', 'city', 'postal_code', 'date_of_birth', 'photo') 

		first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), required=True)
		last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), required=True)
		address = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Address', 'class':'form-control'}), required=True)
		city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City', 'class':'form-control'}), required=True)
		postal_code = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Postal Code', 'class':'form-control'}), required=True)
		date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'yyyy-mm-dd', 'class':'form-control', 'label':'yyyy-mm-dd'}), required=True)
		photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'Photo', 'class':'form-control'}), required=True)


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'address', 'city', 'postal_code', 'date_of_birth', 'photo')

		first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), required=True)
		last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), required=True)
		address = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Address', 'class':'form-control'}), required=True)
		city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City', 'class':'form-control'}), required=True)
		postal_code = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Postal Code', 'class':'form-control'}), required=True)
		date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Date of Birth', 'class':'form-control'}), required=True)
		photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'Photo', 'class':'form-control'}), required=True)