from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=45)

class Modelo(models.Model):
    nombre = models.CharField(max_length=45)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Version(models.Model):
    nombre = models.CharField(max_length=45)
    potencia = models.CharField(max_length=45, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    combustible_com_id = models.IntegerField(null=True, blank=True)

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    garantia = models.IntegerField()
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

class Cliente(models.Model):
    identificacion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)

class Vendedor(models.Model):
    identificacion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=30)

class Pais(models.Model):
    nombre = models.CharField(max_length=45)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Ventas(models.Model):
    fecha_venta = models.DateField()
    precio_final = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
