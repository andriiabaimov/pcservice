from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', RepairListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', RepairDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', RepairDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', RepairUpdateView.as_view(), name='update'),
]
