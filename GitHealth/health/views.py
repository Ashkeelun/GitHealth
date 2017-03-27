from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages import success
from django.http import HttpResponse

# Imports used to serve JSON
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import *

class testAPI(APIView):

    @csrf_exempt
    def post(self, request):
        url = request.data
        repo = Repo(url=url)

        resp = {'instance': repo}

        return Response(resp, status=status.HTTP_200_OK)