from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User # esto ya incluye  nombre y email
from django.urls import reverse # permite construir URLs para las vistas especificas a partir del nombre
from django.template.defaultfilters import slugify

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args,**kwargs)
    

class Publicacion(models.Model):
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=300)
    cuerpo = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField("Categoria", related_name="publicaciones")
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
    def __str__(self):
       return f"{self.titulo} | {self.cuerpo}"
    
    def get_absolute_url(self):
        """
        redirige a la vista 'Inicio'.
        """
        #return reverse('Articulos', args = str(self.id)) #self.if es por los pk q tiene cada art
        return reverse('Inicio') # No es necesario pasar parametros

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo + "-" + str(self.creacion))
        super().save(*args,**kwargs)    
    

class Comentario(models.Model):
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    publicacion = models.ForeignKey("Publicacion",related_name='comentarios',on_delete=models.CASCADE)
    cuerpo = models.CharField(max_length=255)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} | {self.publicacion.titulo}"
    
   
    