from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
      user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
      fullName = models.CharField(max_length=60)
      photo = models.ImageField(upload_to="ClientProfilePics/", null=True, blank=True, default="/unnamed.jpg")

      def __str__(self):
            return str(self.user)


class Visitor(models.Model):
      Organization = models.ForeignKey(to=UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='org_visitors' )
      full_Name = models.CharField(max_length=40)
      contact_Number = models.CharField(max_length=13)
      alternate_Contact_Number = models.CharField(max_length=13, null=True, blank=True)
      email = models.EmailField(null=True, blank=True)
      date_Registered = models.DateTimeField(null=True, blank=True)
      last_visit = models.DateTimeField(null=True, blank=True)


      address = models.TextField(null=True)
      photo = models.ImageField(upload_to="visitors_photos/", null=True, blank=True, default="/default_visitor.png")

      def __str__(self):
            return self.full_Name

class VisitDetails(models.Model):
      Organization = models.ForeignKey(to=UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='org_visits' )
      visitor = models.ForeignKey(to=Visitor, on_delete=models.CASCADE, null=True, blank=True, related_name='visits')
      visit_Number = models.IntegerField(null=True, blank=True)
      visit_Date = models.DateTimeField(null=True, blank=True)
      Description = models.TextField(null=True, blank=True)

      def __str__(self):
            return ("%s, %s") %(self.visitor, self.visit_Number)