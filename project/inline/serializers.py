from rest_framework import serializers
from .models import Profile, FamilyMember

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'created_date']

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['id', 'profile', 'name', 'relationship']
