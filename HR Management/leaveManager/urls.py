from django.conf.urls import url
from leaveManager import views
from leaveManager.views import LeaveDetail

urlpatterns = [
    url(r'^viewLeaves/(?P<pk>\d+)/$', LeaveDetail.as_view(), name='emp-leaves'),
]
