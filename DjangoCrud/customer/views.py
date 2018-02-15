from django.shortcuts import render,reverse,redirect
from .models import Customer
from django.views.generic import CreateView,UpdateView
from .forms import CustomerForm

# Create your views here.
def CustomerDetails(request):
    custObj = Customer.objects.all()
    return render(request,'customer/customer.html',{'cust':custObj})

class CustomerInformation(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/addNewCustomer.html"

    def form_valid(self, form):
        if form.is_valid():
            cust = form.save(commit=False)
            return redirect("cust:addCustomer")
        return super(CustomerInformation, self).form_valid(form)