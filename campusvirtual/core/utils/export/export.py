from io import BytesIO

import pandas as pd
from django.http import HttpResponse


def http_response_excel(df, filename):
    """
    Devuelve un HttpResponse con un archivo .xlsx generado a partir de un pd.DataFrame
    
    Fuentes:
    https://stackoverflow.com/questions/56407199/django-pandas-dataframe-download-as-excel-file
    https://gist.github.com/thomascenni/edcecdfda4d05dbe6aed6f27fc4d36a6
    """

    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename=' + filename
        return response