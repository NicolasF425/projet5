def square(value):
    try:
        square_value = value * value
        return square_value
    except ValueError:
        print("Le paramètre doit être un nombre !")
        return None
