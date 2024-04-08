from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre de la categoria", max_length = 100, null = False, blank=False)
    estado = models.BooleanField("Categoria archivada", default = True)
    fecha_creacion = models.DateTimeField("Fecha de cracion", auto_now_add = True)
    
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres de autor", max_length = 100, null = False, blank=False)
    apellidos = models.CharField("Apellidos de autor", max_length = 100, null = False, blank = False)
    facebook = models.URLField("Facebook", null=True, blank = True)
    instagram = models.URLField("Instagram", null=True, blank = True)
    twitter = models.URLField("Twitter", null=True, blank = True)
    web = models.URLField("Web", null=True, blank = True)
    correo = models.EmailField("Correo electronico", null= False, blank = False)
    estado = models.BooleanField("Autor activo/No activo", default = True)
    fecha_creacion = models.DateField("Fecha de creacion", auto_now_add = True)
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        
    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)
    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("Titulo del post", max_length = 100, null = False, blank = False)
    descripcion = models.CharField("Descripcion del post", max_length = 200, null = False, blank = False)
    contenido = RichTextField("Contenido del post")
    imagen = models.URLField(max_length = 500, null = False, blank = False)
    fecha_publicacion = models.DateField("Fecha de publicacion", auto_now_add = True)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField("Publicado/No publicado")
    slug = models.SlugField(max_length = 50, null = False, blank = False)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.titulo
    