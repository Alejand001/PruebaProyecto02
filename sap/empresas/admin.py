from django.contrib import admin

# Register your models here.
from empresas.models import Contacto, Empresa, Deals, Producto, Standard, Tarea

admin.site.register (Contacto)
admin.site.register (Empresa)
admin.site.register (Deals)
admin.site.register (Producto)
admin.site.register (Standard)
admin.site.register (Tarea)
