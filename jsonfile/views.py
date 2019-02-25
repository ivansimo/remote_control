from django.shortcuts import render
from django.http import HttpResponse





def jsonfile(request):
    return render(request, 'jsonfile/jsonfile.html')
