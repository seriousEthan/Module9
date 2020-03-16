# Ethan Martin
# Module 9

def add(x, y):
    """Add Function"""

    return x + y


def subtract(x, y):
    """Subtract Function"""

    return x - y


def multiply(x, y):
    """Multiply Function"""

    return x * y


def divide(x, y):
    """Divide Function"""

    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y


def c2f(temp):
    """Changes temperature from Celsius to Fahrenheit"""

    c = (temp * 9) / 5 + 32

    b = '%.2f' % c

    return float(b)


def f2c(temp):
    """Changes temperature from Fahrenheit to Celsius"""

    c = 5 / 9 * (temp - 32)

    b = '%.2f' % c

    return float(b)
