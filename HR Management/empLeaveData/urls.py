from django.conf.urls import url
from empLeaveData import views
from .views import EmployeeDetail,EmployeeCreate,DeptCreate
from django.views.generic import DetailView

urlpatterns = [
    # url(r'^main/$',views.getMain),
    url(r'^view/$',views.getEmployeeDetails,name='emp-det'),
    url(r'^empDetails/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name='employee-detail'),
    url(r'^addEmployee/$',EmployeeCreate.as_view(),name='add-employee'),
    url(r'^dept/$',DeptCreate.as_view(),name='add-dept'),
    url(r'^viewDept/$',views.getDeptDetails,name='dept-det')
]