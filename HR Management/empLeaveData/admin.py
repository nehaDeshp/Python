from django.contrib import admin
from .models import Employee,Dept
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id','emp_name','emp_contact','dept_id']
    list_filter = ['dept_id']
    list_editable = ['emp_name','emp_contact']

class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_id', 'dept_name']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Dept,DeptAdmin)