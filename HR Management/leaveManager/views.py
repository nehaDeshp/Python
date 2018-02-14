from django.shortcuts import render
from django.views.generic import DetailView
from .models import LeaveRecords

# Create your views here.
class LeaveDetail(DetailView):
    model = LeaveRecords
    template_name = "leaveManager/viewEmpLeaves.html"

    def get_context_data(self, **kwargs):
        context = super(LeaveDetail, self).get_context_data(**kwargs)
        context['Leave_data'] = "EmployeeLeaves"
        print(context)
        return context
