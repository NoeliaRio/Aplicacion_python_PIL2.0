def td_verbose(td, verbose):
    return td if not verbose else timedelta_to_string(td)

def timedelta_to_string(td):
    """Transforma un timedelta a string en formato %H:%M:%S"""
    parsed = "0:0:0"
    if td:
        hours, remainder = divmod(td.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        parsed = str(round(hours)) + ":" + str(round(minutes)) + ":" + str(round(seconds))
    return parsed