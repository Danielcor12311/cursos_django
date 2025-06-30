from django.db import models

# Create your models here.
class Cursos(models.Model):
    clave = models.CharField(max_length=10, default="123")
    nombre = models.CharField(max_length=100, verbose_name="Curso")
    descripcion = models.TextField(verbose_name="Acerca de: ")
    nivel = models.CharField(max_length=15, verbose_name="level")
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    imagen =models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre
