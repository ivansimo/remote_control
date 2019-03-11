from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nombrecontacto', 'modelo', 'email', 'contact_date')
    lsit_display_link = ('id', 'nombrecontacto')
    search_fields = ('nombrecontacto', 'email', 'modelo')
    lsit_per_page = 25
     

admin.site.register(Contact, ContactAdmin)