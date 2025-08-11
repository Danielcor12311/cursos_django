from django.contrib import admin
from .models import Cursos
from .models import Actividad
# Register your models here.

class FechasModelo(admin.ModelAdmin):
    readonly_fields =('created','updated')
    list_display = ('nombre','nivel')
    search_fields = ('nombre','nivel')
    date_hierarchy = 'created' 
    list_filter = ('nivel',)

admin.site.register(Cursos, FechasModelo)


class AdministrarActividades(admin.ModelAdmin):
    list_display=('id','descripcion')
    search_fields =('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')

admin.site.register(Actividad, AdministrarActividades)