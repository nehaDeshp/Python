from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_id = models.CharField(max_length=5,primary_key=True)
    dept_name = models.CharField(max_length=10)

    def publish(self):
        self.save()

class Employee(models.Model):
    emp_id = models.CharField(max_length=5,primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_contact = models.CharField(max_length=10)
    dept_id =models.ForeignKey(Dept,on_delete=models.CASCADE)

    def publish(self):
        self.save()
