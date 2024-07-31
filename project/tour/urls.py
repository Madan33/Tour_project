from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('about/', views.about, name="about"),

    # User AUthentication 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    
    #curd
    path('places', views.places_list, name="places"),
    path('create_place/',views.create_place,name='create_place'),
    path("place_update/<int:pk>/",views.place_update,name="update_place"),
    path('place_delete/<int:pk>/', views.place_delete, name='place_delete'),

    #Trip
    path('trip/', views.trip_list, name='trip_list'),
    path('trip/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trip/create/', views.trip_create, name='trip_create'),
    path('trip_update/<int:pk>/', views.trip_update, name='trip_update'),
    path('trip_delete/<int:pk>/', views.trip_delete, name='trip_delete'),

    

    #Booking 
    path('booking_create/', views.create_booking, name='create_booking'),
    path('booking_edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('booking_details/', views.booking_detail, name='booking_detail'),
 


    #Enquiry
    path('enquiry/', views.enquiry_form, name='enquiry_form'),
    path('enquiry/success/', views.enquiry_success, name='success'),
    path('categories/', views.category_list, name='category_list'),

    #Package
    path('packages/', views.PackageListView.as_view(), name='package-list'),
    path('packages/create/', views.PackageCreateView.as_view(), name='package-create'),
    path('packages/<int:pk>/', views.PackageDetailView.as_view(), name='package-detail'),
    path('packages/update/<int:pk>/', views.PackageUpdateView.as_view(), name='package-update'),
    path('packages/delete/<int:pk>/', views.PackageDeleteView.as_view(), name='package-delete'),


 




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
