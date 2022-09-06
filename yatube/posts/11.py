def decorator(func):
    def wrapper(a, b):
        if a == b:
            return print(f'площадь квадрата {func(a, b)}')
        else:
            return print(f'площадь прямоугольника {func(a, b)}')

    return wrapper
@decorator
def aaa (a,b):
    