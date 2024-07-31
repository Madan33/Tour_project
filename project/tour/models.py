from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.user.username



GENDER_CHOICES = (('M','Male'),('F','Female'))
CATEGORY_CHOICES = (('B','Family Tours'),('R','Religious Tours'),('S','Solo Trips'),('A','Adventure Trips'))
class Enquiry1(models.Model):
	Name = models.CharField(max_length = 50)
	Gender = models.CharField(choices = GENDER_CHOICES,max_length = 128,default = 'M')
	dob = models.DateField(max_length = 8)
	age = models.IntegerField()
	phone = models.CharField(max_length= 12)
	Email = models.EmailField(max_length = 70,blank = True)
	Category = models.CharField(choices = CATEGORY_CHOICES,max_length = 128)
	No_of_Days = models.IntegerField()
	No_of_Childrens = models.IntegerField()
	No_of_Adults = models.IntegerField()
	Enquiry_message = models.TextField()

	def __unicode__(self):
		return u'%s %s' % (self.Name,self.Gender)
	
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name}" 


class Packages(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    real_category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=200)
    packages = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    information = models.TextField()
    

    def __str__(self):
        return f"{self.real_category}"

     
   
class Places(models.Model):
    name=models.CharField(max_length=100,help_text='name',blank=False)
    location=models.CharField(max_length=100,help_text='location')
    img=models.ImageField(default='media/image.jpg',upload_to='media/images', height_field=None, width_field=None, max_length=100)
    description=models.CharField(max_length=250,help_text='description',default=0)
    places_to_explore=models.CharField(max_length=250,help_text="places to explore",default=0)

    def __str__(self):
        return f"{self.name}"


class Trip(models.Model):
     
     CATEGORY_CHOICES = (
        ('B', 'Family Tours'),
        ('R', 'Religious Tours'),
        ('S', 'Solo Trips'),
        ('A', 'Adventure Trips'),
    )
     place = models.CharField(max_length=100, help_text='Place', blank=False)
     location = models.CharField(max_length=100, help_text='Location', default=0)
     image = models.ImageField(default='media/image.jpg', upload_to='media/images', height_field=None, width_field=None, max_length=100)
     price = models.IntegerField(default=0)
     places_to_explore = models.CharField(max_length=250, help_text='Places to explore', default='')
     start_date = models.DateField()
     end_date = models.DateField()
     packages = models.ManyToManyField(Packages)
     places = models.ManyToManyField(Places)
     
     def __str__(self):
        return f"{self.place} ({self.location})"

class Booking(models.Model):
     
     CATEGORY_CHOICES = (
        ('B', 'Family Tours'),
        ('R', 'Religious Tours'),
        ('S', 'Solo Trips'),
        ('A', 'Adventure Trips'),
    )
     trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
     booking_date = models.DateTimeField(default=timezone.now)
     price = models.IntegerField(default=0)
     name = models.CharField(max_length=150, default="")
     email = models.CharField(max_length=150, default="")
     contact = models.CharField(max_length=15, default="")
     
     class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
        def __str__(self): 
            return f'Booking ID: {self.id} - Trip: {self.trip} - Date: {self.booking_date}'
    
    



