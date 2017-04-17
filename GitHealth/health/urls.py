from django.conf.urls import url

from .views import *

app_name = 'health'

urlpatterns = [
    url(r'^api/$', testAPI.as_view(), name='document_api')
]