def log_decorator(func):
    def wrapper():
        print("Avant la fonction\n")
        result = func()
        print("\nAprès la fonction")
        return result
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
