from django.forms.widgets import DateInput
from django_filters.widgets import SuffixedMultiWidget 

class CustomDateInput(DateInput):
    """
    Clase para generar un input en el que type='date'
    Se sobreescribe DateInput para lograr que input_type='date', lo que permite
    el renderizado del datepicker en buscadores como Chrome o Edge
    """
    def __init__(self, *args, **kwargs):
        self.input_type = 'date'
        super().__init__(*args, **kwargs)


class CustomDateRangeWidget(SuffixedMultiWidget):
    """
    Clase que genera un widget de dos input cuyo type="date" 
    Se sobreescribe DateRangeWidget para lograr que los widgets utilizados
    sean CustomDateInput
    """

    template_name = 'widgets/multiwidget.html'
    suffixes = ['before', 'after']

    def __init__(self, attrs=None):
        widgets = (CustomDateInput, CustomDateInput)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]