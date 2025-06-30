from django.contrib import admin
from .models import Cursos
# Register your models here.

class FechasModelo(admin.ModelAdmin):
    readonly_fields =('created','updated')
    list_display = ('clave','nombre','nivel')
    search_fields = ('clave','nombre','nivel')
    date_hierarchy = 'created' 
    list_filter = ('nivel',)

admin.site.register(Cursos, FechasModelo)