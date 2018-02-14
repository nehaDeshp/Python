from django.contrib import admin
from .models import LeaveRecords
# Register your models here.



class LeaveAdmin(admin.ModelAdmin):
    list_display = ['emp_id','vacation_balance','sick_balance','holiday_balance']

admin.site.register(LeaveRecords, LeaveAdmin)