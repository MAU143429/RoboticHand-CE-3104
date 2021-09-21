def validate_bool(value):
    if str(value) == "True" or str(value) == "False":
        return True
    else:
        return False