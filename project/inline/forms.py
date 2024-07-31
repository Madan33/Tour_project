from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import FamilyMember, Profile




class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()

FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,form=FamilyMemberForm, extra=1)


class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=()
profileformset=inlineformset_factory(Profile, FamilyMember,form=profileform, extra=1)