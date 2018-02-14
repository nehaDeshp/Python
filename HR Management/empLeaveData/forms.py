from django import forms
from .models import Employee,Dept

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_id','emp_name','emp_contact','dept_id')

class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ('dept_id','dept_name',)