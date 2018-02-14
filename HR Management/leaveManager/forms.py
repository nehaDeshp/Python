from django.forms import forms
from .models import LeaveRecords

class LeavesForm(forms.ModelForm):
    class Meta:
        model = LeaveRecords
        fields = ('vacation_balance','sick_balance','holiday_balance',)