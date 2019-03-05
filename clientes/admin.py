from django.contrib import admin

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('empresa','nombre','email','telefono','fecha_de_alta','alerta')
    list_display_links = ('fecha_de_alta',)
    list_editable = ('telefono','alerta')
    search_fields = ('nombre',)
    list_per_page = 8

admin.site.register(Cliente, ClienteAdmin)