from django.contrib import admin
from .models import Profile,FamilyMember,ContactMessage,RelationshipPost



admin.site.register(Profile)
admin.site.register(FamilyMember)
admin.site.register(ContactMessage)
admin.site.register(RelationshipPost)
