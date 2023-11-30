from django.contrib import admin
from core.campus.models import Pais, Provincia, Ciudad, Barrio, Universidad, Facultad, Campus, Programa

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Universidad)
admin.site.register(Facultad)
admin.site.register(Campus)
admin.site.register(Programa)