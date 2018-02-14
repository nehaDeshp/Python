from django.shortcuts import render,redirect
from .models import Employee,Dept
from django.views.generic import DetailView,CreateView
from .forms import EmployeeForm,DeptForm

def getMain(request):
    return render(request,'hrManageData/base.html')

# Create your views here.
def getEmployeeDetails(request):
    employee = Employee.objects.all()
    return render(request, 'hrManageData/view_employees.html', {'empData':employee})

def getDeptDetails(request):
    dept = Dept.objects.all()
    return render(request, 'hrManageData/view_dept.html', {'dept': dept})

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'hrManageData/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetail, self).get_context_data(**kwargs)
        context['Emp_data'] = "Employee"
        return context

class EmployeeCreate(CreateView):
    model=Employee
    template_name = 'hrManageData/add_employee.html'
    form_class = EmployeeForm

    def form_valid(self, form):
        if form.is_valid():
            emp = form.save(commit=False)
            return super(EmployeeCreate,self).form_valid(form)

class DeptCreate(CreateView):
    model=Dept
    template_name = 'hrManageData/add_dept.html'
    form_class = DeptForm

    def form_valid(self, form):
        if form.is_valid():
            dept = form.save(commit=False)
            return super(DeptCreate, self).form_valid(form)



