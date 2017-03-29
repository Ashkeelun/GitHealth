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

from .serializers import UrlSerializer
from .utils import *

class testAPI(APIView):

    # def get(self, request):
    #     url = request.data
    #     repo = Repo(url=r'https://github.com/OSSHealth/ghdata/tree/dev')
    #
    #     # resp = {'instance': repo}
    #
    #     return Response(repo.dir.total_doc_info(), status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        urlSer = UrlSerializer(data=request.data)
        if urlSer.is_valid():
            url = urlSer.data['url']
            repo = Repo(url=url)
            return Response(repo.dir.total_doc_info(), status=status.HTTP_200_OK)