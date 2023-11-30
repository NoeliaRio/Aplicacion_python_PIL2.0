from datetime import timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils.managers import TimeFramedModelManager
from core.utils.datetime.timedelta import timedelta_to_string

def status_verbose(object_status: str, all_status: dict):
    """
    Devuelve el estado de un objeto de forma legible para el usuario.
    
    Los estados del objeto deben estar definidos de la siguiente manera:

    ESTADO_A = 'estado_a'
    ESTADO_B = 'estado_b'

    STATUS = [
        (ESTADO_A, 'Estado A verboso'),
        (ESTADO_B, 'Estado B verboso')
    ]

    'object_status' debe contener el valor de la constante de uno de los estados.
    'all_status' debe contener el diccionario 'STATUS'.
    """
    status_verbose = None
    for status in all_status:
        if object_status in status:
            status_verbose = status[1]
            break
    return status_verbose

class TimeFramedModel(models.Model):
    """
    An abstract base class model that provides ``start``
    and ``end`` fields to record a timeframe.

    From: https://github.com/jazzband/django-model-utils/blob/master/model_utils/models.py
    """
    WAITING = 'waiting'
    STARTED = 'started'
    FINISHED = 'finished'

    STATUS = [
        [WAITING, 'En espera'],
        [STARTED, 'Iniciado'],
        [FINISHED, 'Finalizado'],
    ]

    start = models.DateTimeField(_('inicio'), null=True, blank=True)
    end = models.DateTimeField(_('fin'), null=True, blank=True)
    objects = TimeFramedModelManager()

    class Meta:
        abstract = True

    def status(self):
        status = 'undefined'
        if not self.start and not self.end:
            return TimeFramedModel.WAITING
        if self.start and not self.end:
            return TimeFramedModel.STARTED
        if self.start and self.end:
            return TimeFramedModel.FINISHED
        else:
            return status

    def status_verbose(self):
        return status_verbose(self.status(), TimeFramedModel.STATUS)

    def duration(self):
        """
        Devuelve un datetime.timedelta con la diferencia entre el tiempo 
        de finalización y el tiempo de inicio. 
        Si el marco de tiempo no ha finalizado, devuelve 'timedelta(0)'
        """
        duration = timedelta(seconds=0)
        if self.start and self.end:
            duration = self.end - self.start
        return duration