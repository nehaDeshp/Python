from django.urls import path
from django.conf.urls import url
from add_product import views

urlpatterns = [
    url('display/',views.displayProd),
    url(r'^prod/(?P<pk>\d+)/$', views.prod_detail, name='prod_detail'),
    url(r'^prod/add/$', views.addProd, name='addProd')
]