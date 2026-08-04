from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    url = models.URLField(blank=True, verbose_name='URL')

#devuelve el nombre del proyecto en el panel de administración
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
