from django.db import models

# Create your models here.
class Cruc2022(models.Model):
    Palabra = models.CharField(max_length=100)
    Temperatura_2 = models.CharField(max_length=1000)
    Temperatura_7 = models.CharField(max_length=1000)
    Frecuencia = models.CharField(max_length=10)
    Valida = models.BooleanField(default=True)
    Letras = models.IntegerField()
    _1a_letra = models.CharField(max_length=10, default=None)
    _2a_letra = models.CharField(max_length=10, default=None)
    _3a_letra = models.CharField(max_length=10, default=None)
    _4a_letra = models.CharField(max_length=10, default=None)
    _5a_letra = models.CharField(max_length=10, default=None)
    _6a_letra = models.CharField(max_length=10, default=None)
    _7a_letra = models.CharField(max_length=10, default=None)
    _8a_letra = models.CharField(max_length=10, default=None)
    _9a_letra = models.CharField(max_length=10, default=None)
    _10a_letra = models.CharField(max_length=10, default=None)
    _11a_letra = models.CharField(max_length=10, default=None)
    _12a_letra = models.CharField(max_length=10, default=None)
    _13a_letra = models.CharField(max_length=10, default=None)
    _14a_letra = models.CharField(max_length=10, default=None)
    _15a_letra = models.CharField(max_length=10, default=None)



    def __str__(self):
        return self.name