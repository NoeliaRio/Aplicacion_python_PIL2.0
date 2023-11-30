import locale

"""
https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-the-view-and-template-in-django
"""

def datetime_verbose(date_time):
    try:
        locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8') #your language encoding
    except:
        locale.setlocale(locale.LC_TIME, 'es_AR')

    translated_date = date_time.strftime("%d de %B de %Y a las %H:%M")
    return translated_date