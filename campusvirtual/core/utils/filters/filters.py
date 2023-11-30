from core.utils.fields.fields import CustomDateRangeField
from django_filters.filters import DateFromToRangeFilter

class CustomDateFromToRangeFilter(DateFromToRangeFilter):
    
    def __init__(self, *args, **kwargs):
        self.field_class = CustomDateRangeField
        super().__init__(*args, **kwargs)