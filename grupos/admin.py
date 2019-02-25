from django.contrib import admin

from .models import Grupo

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('cliente','modelo','ciudad','puesta_en_marcha','averiado')
    list_display_links = ('cliente','puesta_en_marcha')
    list_filter = ('ciudad',)
    list_editable = ('averiado',)
    search_fields = ('marca','cp')
    list_per_page = 8

admin.site.register(Grupo, GrupoAdmin)