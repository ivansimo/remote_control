from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import cliente_choices, kva_choices, código_choices, ciudad_choices
from .models import Grupo

def index(request):
    grupos = Grupo.objects.order_by('-puesta_en_marcha').filter(averiado=True)

    paginator = Paginator(grupos, 6)
    page = request.GET.get('page')
    paged_grupos = paginator.get_page(page)

    context = {
        'grupos': paged_grupos
    }

    return render(request, 'grupos/grupos.html', context)

def grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    context = {
        'grupo': grupo
    }

    return render(request, 'grupos/grupo.html', context)
    
def search(request):
    queryset_list = Grupo.objects.order_by('-última_revisión')

    # Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(descripción__icontains=keywords)

    # Buscar por kva
    if 'kva' in request.GET:
        kva = request.GET['kva']
        if kva:
            queryset_list = queryset_list.filter(kva__lte=kva)

    # Buscar por código
    if 'código_avería' in request.GET:
        código_avería = request.GET['código_avería']
        if código_avería:
            queryset_list = queryset_list.filter(código_avería__iexact=código_avería)

    # Buscar por kva
    if 'ciudad' in request.GET:
        ciudad = request.GET['ciudad']
        if ciudad:
            queryset_list = queryset_list.filter(ciudad__iexact=ciudad)

    # Buscar por kva
    if 'cliente' in request.GET:
        cliente = request.GET['cliente']
        if cliente:
            queryset_list = queryset_list.filter(cliente__icontains=cliente)
    

    context ={
        'kva_choices': kva_choices,
        'código_choices': código_choices,
        'ciudad_choices': ciudad_choices,
        'cliente_choices': cliente_choices,
        'grupos': queryset_list,
        'values': request.GET
    }
    return render(request, 'grupos/search.html', context)

    def jsondata(request):
        return render(request, 'grupos/jsondata.html')