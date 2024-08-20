from django.shortcuts import render, redirect
from api.models import UploadedFile


def index(request):
    files = UploadedFile.objects.all()
    return render(request, 'index.html',{'files': files})