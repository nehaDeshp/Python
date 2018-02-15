from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fname','lname','room_no','email','address','checkin','checkout','contact','stay_time')