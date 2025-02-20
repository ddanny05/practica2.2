from django.db import models

class Clientes(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True,)
    nombre = models.CharField(max_length=50,)
    apellido = models.CharField(max_length=50,)
    direccion = models.CharField(max_length=100,)
    telefono = models.CharField(max_length=15,)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'
    def __str__(self):
        return f'{self.cedula} -- {self.nombre} -- {self.apellido}'
