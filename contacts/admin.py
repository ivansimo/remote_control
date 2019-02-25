from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'modelo', 'email', 'contact_date')
    lsit_display_link = ('id', 'name')
    search_fields = ('name', 'email', 'modelo')
    lsit_per_page = 25
     

admin.site.register(Contact, ContactAdmin)