def square(value):
    try:
        square_value = value ** 2
    except ValueError:
        print("Le paramètre doit être un nombre !")
        return None
    return square_value
