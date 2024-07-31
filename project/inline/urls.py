from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'family-members', views.FamilyMemberViewSet)    


urlpatterns = [

    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('about_us/',views.about_us,name="about_us"),
    path('profile_create/', views.profile_create, name='profile_create'),
    path('profile/<int:pk>/edit/',views. profile_edit, name='edit_profile'),
    path('profile/<int:pk>/delete/', views.profile_delete, name='delete_profile'),
    path('view_profiles',views.view_profiles,name='view_profiles_with_family_members'),
    
    #DRF
    


    # CONtact
    path("contact_messages/",views.contact_messages,name="contact_messages"),

    
]
  






