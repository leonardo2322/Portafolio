from django.db import models

# Create your models here.
class Enlace(models.Model):
    url = models.URLField(max_length=200)
    imagen = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.url
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    enlace = models.URLField(max_length=200,verbose_name="Enlace")
    imagen = models.ImageField(upload_to='project/')
    detalles = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    titulo = models.CharField(max_length=50)
    enlaces = models.ManyToManyField(Enlace, blank=True)
    
    def __str__(self):
        return self.titulo
    

class Technologia(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tech/')
    
    def __str__(self):
        return self.nombre
    
class Reconocimiento(models.Model):
    titulo = models.CharField( max_length=50)
    Descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='reconocimient/')


    def __str__(self):
        return self.titulo