from django.contrib import admin
from core.models import Carrera
from core.models import Docente

# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    pass
admin.site.register(Carrera,CarreraAdmin)

class DocenteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Docente,DocenteAdmin)