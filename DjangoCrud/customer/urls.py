from django.urls import path,reverse
from customer import views
from .models import Customer

app_name='cust'

urlpatterns = [
    path('customers/',views.CustomerDetails,name='viewCustomer'),
    path('customers/add',views.CustomerInformation.as_view(),name='addCustomer'),
]
