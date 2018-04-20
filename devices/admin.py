from django.contrib import admin
from .models import router

class routerAdmin(admin.ModelAdmin):
    list_display = ('hostname','macaddress',)
    list_display_links = ('hostname', 'macaddress',) 
     
    list_per_page = 25

# Register your models here.
admin.site.register(router, routerAdmin)
