from django.db import models

class TimeFramedModelManager(models.Manager):
    def filter_by_time_range(self, start, end):
        return self.filter(start__range=[start, end]).order_by('start')

    