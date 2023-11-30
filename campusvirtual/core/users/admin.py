from django.contrib import admin
from core.users.models import User, Genero, TipoUser

# Register your models here.
admin.site.register(User)
admin.site.register(Genero)
admin.site.register(TipoUser)