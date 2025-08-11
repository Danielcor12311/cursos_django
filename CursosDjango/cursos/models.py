from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Curso")
    descripcion = models.TextField(verbose_name="Acerca de: ")
    nivel = models.CharField(max_length=15, verbose_name="Nivel")
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave Actividad")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    descripcion = RichTextField(verbose_name="Descripción: ")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]
    def __str__(self):
        return self.descripcion 