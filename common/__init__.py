def try_parse_int(value):
    try:
        return int(value)
    except ValueError:
        return value
