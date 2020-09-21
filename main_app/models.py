from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
      user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
      fullName = models.CharField(max_length=60)

      def __str__(self):
            return str(self.user)


class Visitor(models.Model):
      Organization = models.ForeignKey(to=UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='org_visitors' )
      full_Name = models.CharField(max_length=40)
      contact_Number = models.CharField(max_length=13)
      alternate_Contact_Number = models.CharField(max_length=13)
      email = models.EmailField(null=True, blank=True)
      first_Visit = models.DateTimeField(null=True, blank=True)


      address = models.TextField(null=True, blank=True)

      def __str__(self):
            return self.full_Name