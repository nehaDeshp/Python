from django.db import models

# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contact = models.IntegerField()
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    room_no = models.IntegerField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    stay_time = models.IntegerField()
