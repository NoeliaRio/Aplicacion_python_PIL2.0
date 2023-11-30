from datetime import datetime as dt, time

from django.forms.fields import DateField
from django_filters.fields import RangeField
from django_filters.utils import handle_timezone

from core.utils.widgets.widgets import CustomDateInput, CustomDateRangeWidget

class CustomDateField(DateField):
    """
    Se sobreescribe DateField para lograr que el input utilizado sea CustomDateInput
    """
    def __init__(self, *args, **kwargs):
        self.widget = CustomDateInput
        super().__init__(*args, **kwargs)


class CustomDateRangeField(RangeField):
    """
    Se sobreescribe DateRangeField para poder utilizar CustomDateRangeWidget y 
    CustomDateField
    """
    widget = CustomDateRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            CustomDateField(),
            CustomDateField()
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            start_date, stop_date = data_list
            if start_date:
                start_date = handle_timezone(
                    dt.combine(start_date, time.min),
                    False
                )
            if stop_date:
                stop_date = handle_timezone(
                    dt.combine(stop_date, time.max),
                    False
                )
            return slice(start_date, stop_date)
        return None