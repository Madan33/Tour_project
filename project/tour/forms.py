from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Profile,Trip,Booking,Enquiry1,Packages,Places
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


#AuthenticationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['name', 'location', 'img', 'description', 'places_to_explore']


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['place', 'location', 'image', 'price', 'places_to_explore', 'start_date', 'end_date', 'packages', 'places']

    places = forms.ModelMultipleChoiceField(queryset=Places.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['trip', 'booking_date', 'price', 'name', 'email', 'contact']

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry1
        fields = ['Name', 'Gender', 'dob', 'age', 'phone', 'Email', 'Category', 'No_of_Days', 'No_of_Childrens', 'No_of_Adults', 'Enquiry_message']


class packagesform(forms.ModelForm):
    class Meta:
        model=Packages
        fields=['category','real_category','subcategory','price','packages','information']
