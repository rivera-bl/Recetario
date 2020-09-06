from django.db import models

class Receta(models.Model):
    title = models.CharField(verbose_name="Título", max_length=50)
    subtitle = models.CharField(verbose_name="Título", max_length=100)
    image = models.ImageField(verbose_name="Imagen", upload_to="recetas")
    ingredients = models.TextField(verbose_name="Ingredientes")
    preparation = models.TextField(verbose_name="Preparacíon")  
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ['created']

    def __str__(self):
        return self.title
