from django.shortcuts import render
from django.http import HttpResponse
from grupos.choices import cliente_choices, kva_choices, código_choices, ciudad_choices

from grupos.models import Grupo
from clientes.models import Cliente


def index(request):
    grupos = Grupo.objects.order_by('-fecha_avería').filter(averiado=True)[:3]

    context = {
        'grupos': grupos,
        'cliente_choices': cliente_choices,
        'código_choices': código_choices,
        'kva_choices': kva_choices,
        'ciudad_choices': ciudad_choices
    }
    
    return render(request, 'pages/index.html', context)

def alertas(request):
    # GET ALL CLIENTES
    clientes = Cliente.objects.order_by('-fecha_de_alta')

    # GET ALERTA
    alerta = Cliente.objects.all().filter(alerta=True)

    context = {
       'clientes': clientes,
       'alerta': alerta,
     }

    return render(request, 'pages/alertas.html', context)