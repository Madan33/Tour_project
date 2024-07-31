from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# inline forms Models 
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)


class RelationshipPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} - {self.email}'
