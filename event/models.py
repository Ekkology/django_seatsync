from django.db import models

class Event(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    configuracion = models.JSONField(default=dict, blank=True, null=True)  # Asegúrate de usar el campo correcto
    
class chair(models.Model):
    numero = models.IntegerField(unique=True)
    posicion_x = models.IntegerField()
    posicion_y = models.IntegerField()
    estado = models.CharField(max_length=20, default='disponible')
    evento = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='chairs', null=True)

    def __str__(self):
        return f'Chair {self.numero}'