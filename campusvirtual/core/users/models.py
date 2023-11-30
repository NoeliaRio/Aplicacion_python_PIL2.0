from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel


class Genero(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de género', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Género")
        verbose_name_plural = ("Géneros")
        ordering = ["name"]
        db_table = 'genero'

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    ADMINISTRATOR = 'Administrador'
    USUARIO = 'Usuario'
    updated_at = models.DateTimeField('Fecha de modificación', null=True)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, verbose_name='Tipo de usuario', null=True)

    class Meta:
        ordering = ["username"]
            
    def validate_administrator(value):
        is_admin = False
        u = User.objects.get(id=value)
        
        for g in u.groups.all():
            if g.name == 'Administrador':
                is_admin = True

        if not is_admin:
            raise ValidationError(
                _('%(name)s no es un administrador'),
                params={'name': u.username},
            )
    def __str__(self):
        return self.first_name + " " + self.last_name

    def is_admin(self):
        is_admin = False
        for g in self.groups.all():
            if g.name == self.ADMINISTRATOR:
                is_admin = True
        return is_admin

    def toJSON(self):
        dict = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.first_name + " " + self.last_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'administrator': self.is_admin(),
        }
        return dict
    

class TipoUser(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de tipo', max_length=150, unique=True)


    class Meta:
        verbose_name = ("Tipo de usuario")
        verbose_name_plural = ("Tipos de usuario")
        ordering = ["name"]
        db_table = 'tipo_user'

    def __str__(self):
        return f'{self.name}'
    

