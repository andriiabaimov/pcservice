from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^repairs/$', RepairListView.as_view(), name='repairs_list'),
    url(r'^repairs/(?P<pk>\d+)/$', RepairDetailView.as_view(), name='repair'),
    url(r'^repairs/(?P<pk>\d+)/delete/$', RepairDeleteView.as_view(), name='delete_repair'),
    url(r'^repairs/(?P<pk>\d+)/update/$', RepairUpdateView.as_view(), name='update_repair'),
]
