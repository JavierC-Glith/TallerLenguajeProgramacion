from django.contrib import admin
from core.models import Habitacion

# Register your models here.
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero','ocupada')
    pass
admin.site.register(Habitacion,HabitacionAdmin)
