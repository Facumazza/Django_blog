from django.contrib import admin
from .models import Categoria, Autor, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        

class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor
    
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ("nombre", "estado", "fecha_creacion",)
    resource_clases = CategoriaResource
    
class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["nombres", "apellidos", "correo"]
    list_display = ("nombres", "apellidos", "correo", "fecha_creacion",)
    resource_clases = AutorResources
    


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)