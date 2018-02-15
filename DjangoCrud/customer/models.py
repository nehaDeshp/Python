from django.db import models

# Create your models here.
class Customer(models.Model):

    K = 'K'
    Q = 'Q'
    T = 'T'
    SM = 'Smoking'
    NS = 'NonSmoking'
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contact = models.IntegerField()
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    room_no = models.IntegerField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    stay_time = models.IntegerField()
    bed_types = (

        (K,"King"),
        (Q,"Queen"),
        (T,"Twin")
    )
    bed_type = models.CharField(max_length=5,choices=bed_types,default=K)

    SMOKING = (
        (SM,"Smoking"),
        (NS,"Non Smoking")
    )
    smoking_type = models.CharField(max_length=12,choices=SMOKING,default=NS)

