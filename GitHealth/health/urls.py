from django.conf.urls import url

from .views import *

app_name = 'health'

urlpatterns = [
    url(r'^test/$', testAPI.as_view(), name='pi_list')
]