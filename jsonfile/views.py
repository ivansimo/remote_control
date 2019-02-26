from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Grupo, Cliente


def jsonfile(request):
    return render(request, 'jsonfile/jsonfile.html')


def grupo(request):

    context = {
        'grupo': grupo,
        'cliente': cliente
    }
    return render(request, 'jsonfile/jsonfile.html', context)