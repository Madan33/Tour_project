from .serializers import ProfileSerializer, FamilyMemberSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import FamilyMemberForm, FamilyMemberFormSet
from .models import FamilyMember,Profile,ContactMessage
from django.views.decorators.csrf import csrf_protect
from .forms import profileform,FamilyMemberForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import viewsets
from django.conf import settings
from django.views import View 
from django.db.models import Q 
from . import forms,models
import os

def home (request):
    return render(request, 'home/index.html')


def about_us(request):
    return render (request,"aboutus/about.html")

#inline forms to create views

def profile_create(request):
    if request.method == 'POST':
        profile_form = profileform(request.POST)
        family_member_formset = FamilyMemberFormSet(request.POST)

        if profile_form.is_valid() and family_member_formset.is_valid():
            profile = profile_form.save()
            family_member_formset.instance = profile
            family_member_formset.save()

            return redirect('index')
    else:
        profile_form = profileform()
        family_member_formset = FamilyMemberFormSet()

    return render(request, 'inline/profile_with_family_members.html', {
        'profile_form': profile_form,
        'family_member_formset': family_member_formset
    })

#Creating curd operations inline forms

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile_form = profileform(request.POST, instance=profile)
        family_member_formset = FamilyMemberFormSet(request.POST, instance=profile)

        if profile_form.is_valid() and family_member_formset.is_valid():
            profile = profile_form.save()
            family_member_formset.save()
            return redirect('index')
    else:
        profile_form = profileform(instance=profile)
        family_member_formset = FamilyMemberFormSet(instance=profile)

    return render(request, 'inline/profile_with_family_members.html', {
        'profile_form': profile_form,
        'family_member_formset': family_member_formset
    })

def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')
    return render(request, 'inline/delete_profile_confirm.html', {'profile': profile})


#To display all Django Admin panel

def view_profiles (request):
    profiles = Profile.objects.all().prefetch_related('familymember_set')
    return render(request, 'inline/profiles1_with_family_members.html', {'profiles': profiles})



#COntact
def contact_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'contact/contacts.html', {'messages': messages})



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
