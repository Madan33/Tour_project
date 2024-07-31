from .forms import PlaceForm ,TripForm,BookingForm,SignUpForm,EnquiryForm
from tour.models import Places,Trip,Booking,Profile,Enquiry1,Category,Packages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.views import View 
from . import forms,models
import os



def index(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "about/about.html")

#Authentication
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        return redirect('index') 
    else:
        return render(request, 'registration/login.html')


def logout(request):
    logout(request)
    return redirect('login')  

# About Places
def places_list(request):
   place=Places.objects.all()
   return render(request, "place/places.html",{'place':place})  

# Create an place
def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            img = form.cleaned_data['img']
            description = form.cleaned_data['description']
            places_to_explore = form.cleaned_data['places_to_explore']

            new_place = Places(
                name=name,
                location=location,
                img=img,
                description=description,
                places_to_explore=places_to_explore
            )
            new_place.save()
            
            return redirect('index')
    else:
        form = PlaceForm()
    return render(request, 'place/place_form.html', {'form': form})

# Edit an PLace
def place_update(request, pk):
    place = get_object_or_404(Places, pk=pk)
    
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = PlaceForm(instance=place)
    
    context = {
        'form': form,
        'pk': pk, 
    }
    return render(request, 'place/edit_place.html', context)

# Delate an place
def place_delete(request, pk):
    place = get_object_or_404(Places, id=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('index')  
    
    return render(request, 'place/delete_place.html', {'place': place})

# TriP
def trip_list(request):
    trips_list = Trip.objects.all()
    paginator = Paginator(trips_list, 1)  

    page_number = request.GET.get('page')
    try:
        trips = paginator.page(page_number)
    except PageNotAnInteger:
        
        trips = paginator.page(1)
    except EmptyPage:
        
        trips = paginator.page(paginator.num_pages)
        return redirect(f'page={paginator.num_pages}')  

    context = {
        'trips': trips,
    }
    return render(request, 'trip/trip_list.html', context)

def trip_detail(request, pk):
    trip = Trip.objects.get(pk=pk)
    context = {
        'trip': trip
    }
    return render(request, 'trip/trip_detail.html', context)

def trip_create(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'trip/trip_form.html', {'form': form})

def trip_update(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trip/trip_form.html', {'form': form})

def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    return render(request, 'trip/trip_confirm_delete.html', {'trip': trip})

#Booking Trip
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_detail')
    else:
        form = BookingForm()
    return render(request, 'booking_trip/create_booking.html', {'form': form})

def edit_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_trip/edit_booking.html', {'form': form})

def booking_detail(request ):
    booking =Booking.objects.all()
    context={
        'booking':booking
    }
    return render(request, 'booking_trip/booking_detail.html', context)

# ABout Enquiry
def enquiry_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_success')  
    else:
        form = EnquiryForm()
    
    return render(request, 'enquiry/enquiry_form.html', {'form': form})

def enquiry_success(request):
    return render(request, 'enquiry/enquiry_success.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'enquiry/category_list.html', {'categories': categories})

#CLasss Based Views for Packages
class PackageListView(ListView):
    model = Packages
    template_name = 'package/package_list.html'  
    context_object_name = 'packages' 

    
class PackageDetailView(DetailView):
    model = Packages
    template_name = 'package/package_detail.html'  
    context_object_name = 'package'  

class PackageCreateView(CreateView):
    model = Packages
    template_name = 'package/package_form.html'  
    fields = ['category', 'real_category', 'subcategory', 'packages', 'price', 'information']
    success_url = reverse_lazy('package-list')  

class PackageUpdateView(UpdateView):
    model = Packages
    template_name = 'package/package_form.html'  
    fields = ['category', 'real_category', 'subcategory', 'packages', 'price', 'information']
    success_url = reverse_lazy('package-list')  

class PackageDeleteView(DeleteView):
    model = Packages
    template_name = 'package/package_confirm_delete.html'  
    success_url = reverse_lazy('package-list')  





