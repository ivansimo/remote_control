from django.shortcuts import render, redirect
from django.http import HttpResponse



def jsonfile(request):
    return render(request, 'jsonfile/jsonfile.html')


