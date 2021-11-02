from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombreT = models.CharField(max_length=255)
    repetir = models.CharField(max_length=255)
    relacionado = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    prioridad = models.CharField(max_length=255)

    def __str__(self):
        return f'Tarea {self.id}:{self.nombreT}:{self.repetir}: {self.relacionado}:{self.descripcion}:{self.prioridad}'


class Standard(models.Model):
    estadoD = models.CharField(max_length=255)

    def __str__(self):
        return f'Empresa {self.id}:{self.estadoD}'


class Producto(models.Model):
    nombreP = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precioU = models.CharField(max_length=255)
    productoA = models.CharField(max_length=255)

    def __str__(self):
        return f'Producto {self.id}:{self.nombreP}:{self.codigo}: {self.categoria}:{self.precioU}:{self.productoA}'


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    sitioweb = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)

    def __str__(self):
        return f'Empresa {self.id}:{self.nombre}:{self.telefono}: {self.sitioweb}:{self.descripcion}:{self.calle}: {self.ciudad}: {self.estado}: {self.pais}: {self.codigo} '


class Contacto(models.Model):
    nombreC = models.CharField(max_length=255)
    apellidoC = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    celular = models.CharField(max_length=255)
    telefonoC = models.CharField(max_length=255)
    teleCasaC = models.CharField(max_length=255)
    suscripcion = models.CharField(max_length=255)
    descripcionC = models.CharField(max_length=255)

    def __str__(self):
        return f'Contacto {self.id}: {self.nombreC}: {self.apellidoC}:{self.titulo}:{self.correo}:{self.celular}:{self.telefonoC}: {self.teleCasaC}: {self.suscripcion}: {self.descripcionC}'


class Deals(models.Model):
    nombreD = models.CharField(max_length=255)
    Monto = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)


    def __str__(self):
        return f'Deals {self.id}: {self.nombreD}: {self.monto}:{self.fecha}:{self.descripcion}'