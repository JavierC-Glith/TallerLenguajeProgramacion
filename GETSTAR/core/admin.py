from django.contrib import admin
from core.models import Comunicado
from core.models import Categoria
# Register your models here.

class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','nivel')
    ordering = ('-fecha_envio',)
    search_fields = ('titulo',)
    pass
admin.site.register(Comunicado,ComunicadoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    pass
admin.site.register(Categoria,CategoriaAdmin)


