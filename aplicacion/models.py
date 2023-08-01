from django.db import models

# Modelo para los cortes
class Corte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = models.IntegerField()
    es_para_nina = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.nombre} {self.precio} ({self.duracion_minutos})"

    

# Modelo para los peinados
class Peinado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.precio} ({self.duracion_minutos})"

# Modelo para los estilistas
class Estilista(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    especialidad = models.CharField(max_length=100)
    experiencia_anios = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.especialidad} ({self.experiencia_anios})"
