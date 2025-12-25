from django.db import models
from django.conf import settings

# Importaciones necesarias para el manejo de archivos
import os
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.
# 1.- Catalogo de Posgrados
class PostgraduateProgram(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Nombre del Posgrado")

    def __str__(self):
        return self.name

# 2.- Modelo de registro de las caracteristicas de las Tesis
class Tesis(models.Model):
    # Datos principales
    titulo = models.CharField(max_length=500, verbose_name="Titulo")
    autor_name = models.CharField(max_length=255, verbose_name="Nombre del Autor")

    # Directores
    director = models.CharField(max_length=255, verbose_name="Director de Tesis")
    codirector = models.CharField(max_length=255, blank=True, null=True, verbose_name="Codirector de Tesis")

    # Relacion con Posgrado
    program = models.ForeignKey(
        PostgraduateProgram,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Tipo de Posgrado"
    )

    publication_year = models.IntegerField(verbose_name="Año")
    abstract = models.TextField(verbose_name="Resumen/Abstract")

    # Archivo PDF
    pdf_file = models.FileField(upload_to='tesis_pdfs/', verbose_name="Archivo PDF")

    # Fecha de creacion
    created_at = models.DateTimeField(auto_now_add=True)

    # Fecha de actualizacion
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

# 3.- Señal para eliminar el archivo PDF cuando se elimina el objeto Tesis
@receiver(post_delete, sender=Tesis)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Borra el archivo del sistema de archivos cuando se elimina el objeto `Tesis` correspondiente.
    """
    if instance.pdf_file:
        if os.path.isfile(instance.pdf_file.path):
            try:
                os.remove(instance.pdf_file.path)
                print(f"Archivo eliminado correctamente: {instance.pdf_file.path}")
            except Exception as e:
                print(f"Error al eliminar archivo: {e}")