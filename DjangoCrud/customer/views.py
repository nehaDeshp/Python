from django.shortcuts import render,reverse,redirect
from .models import Customer
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from .forms import CustomerForm

# Create your views here.
# def CustomerDetails(request):
#     custObj = Customer.objects.all()
#     return render(request,'customer/customer.html',{'cust':custObj})

class CustomerInformation(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/addNewCustomer.html"

    def form_valid(self, form):
        if form.is_valid():
            cust = form.save(commit=True)
            print("done")
            return redirect("cust:addCustomer")
        return super(CustomerInformation, self).form_valid(form)

class CustomerDetails(ListView):
    model = Customer
    template_name = "customer/customer.html"

    def get_context_data(self, **kwargs):
        context = super(CustomerDetails, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context