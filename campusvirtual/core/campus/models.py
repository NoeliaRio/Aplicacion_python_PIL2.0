from django.db import models
from django_softdelete.models import SoftDeleteModel

from core.users.models import User, TipoUser


class Universidad(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de universidad', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Universidad")
        verbose_name_plural = ("Universidades")
        ordering = ["name"]
        db_table = 'universidad'

    def __str__(self):
        return f'{self.name}'
        


class Facultad(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de facultad', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Facultad")
        verbose_name_plural = ("Facultades")
        ordering = ["name"]
        db_table = 'facultad'

    def __str__(self):
        return f'{self.name}'


class Campus(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de campus', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Campus")
        verbose_name_plural = ("Campuses")
        ordering = ["name"]
        db_table = 'campus'

    def __str__(self):
        return f'{self.name}'


class Programa(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de programa', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Programa")
        verbose_name_plural = ("Programas")
        ordering = ["name"]
        db_table = 'programa'

    def __str__(self):
        return f'{self.name}'


class Carrera(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.PROTECT, verbose_name='Universidad')
    facultad = models.ForeignKey(Facultad, on_delete=models.PROTECT, verbose_name='Facultad')
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name='Campus')
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')


    class Meta:
        verbose_name = ("Campus")
        verbose_name_plural = ("Campuses")
        ordering = ["id"]
        db_table = 'carrera'

    def __str__(self):
        return f'{self.id}'
    

class UserCarrera(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='usuario',
        verbose_name='Usuario')
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, verbose_name='Carrera')
    tipo_user = models.ForeignKey(TipoUser, on_delete=models.PROTECT, verbose_name='Tipo de usuario')

    class Meta:
        verbose_name = ("Campus")
        verbose_name_plural = ("Campuses")
        ordering = ["id"]
        db_table = 'usercarrera'

    def __str__(self):
        return f'{self.id}'


class Pais(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de país', max_length=150, unique=True)


    class Meta:
        verbose_name = ("País")
        verbose_name_plural = ("Países")
        ordering = ["name"]
        db_table = 'pais'

    def __str__(self):
        return f'{self.name}'


class Provincia(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de provincia', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Provincia")
        verbose_name_plural = ("Provincias")
        ordering = ["name"]
        db_table = 'provincia'

    def __str__(self):
        return f'{self.name}'
    

class Ciudad(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de ciudad', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Ciudad")
        verbose_name_plural = ("Ciudades")
        ordering = ["name"]
        db_table = 'ciudad'

    def __str__(self):
        return f'{self.name}'
    

class Barrio(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de barrio', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Barrio")
        verbose_name_plural = ("Barrios")
        ordering = ["name"]
        db_table = 'barrio'

    def __str__(self):
        return f'{self.name}'
    

class Lugar(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, verbose_name='País')
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, verbose_name='Provincia')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, verbose_name='Ciudad')
    barrio = models.ForeignKey(Barrio, on_delete=models.PROTECT, verbose_name='Barrio')


    class Meta:
        verbose_name = ("Lugar")
        verbose_name_plural = ("Lugares")
        ordering = ["id"]
        db_table = 'lugar'

    def __str__(self):
        return f'{self.barrio.name} - {self.ciudad.name} ({self.provincia.name} - {self.pais.name})'