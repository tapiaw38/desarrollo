from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    fecha = models.DateField()
    cuil = models.CharField(max_length=11,null=True,blank=True)
    tipo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    cbu =  models.CharField(max_length=22,null=True,blank=True)
    tel = models.CharField(max_length=10, null=True, blank=True)

    estado = models.BooleanField(default=False)
    observacion = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.dni)