from django.db import models
from django.utils import timezone
from User_App.models import CustomUser

# Create your models here.
class Events(models.Model):
    """ serialize Event objects"""
    Event_Name = models.CharField(null=False, max_length=150, blank=False) 
    Number_of_tickets= models.IntegerField(default=500)
    Event_description = models.CharField(null=True, max_length=200)
    Email = models.CharField(null=False, max_length=200) 
    Event_Date = models.DateField(default=timezone.now)
    Events_members = models.ManyToManyField(CustomUser, blank=True )
    Created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Event")
    
    
    def __str__(self):
        return self.Event_Name
