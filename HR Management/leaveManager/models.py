from django.db import models
from empLeaveData.models import Employee

# Create your models here.
class LeaveRecords(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE,primary_key=True)
    vacation_balance = models.IntegerField()
    sick_balance = models.IntegerField()
    holiday_balance = models.IntegerField()

    def publish(self):
        self.save()
