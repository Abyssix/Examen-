from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Casa

class CasaAdmin(admin.ModelAdmin):
    list_display =('ubicacion', 'precio', 'disponibilidad')
    
# Register your models here.
admin.site.register(Casa, CasaAdmin)
