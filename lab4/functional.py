import math


def f(x, derivative_order):
    if derivative_order == 0:
        return ((math.sin(x + math.pi / 2)) ** 2 - (x ** 2) / 4)
    elif derivative_order == 1:
        return ((-x) / 2 - 2 * math.sin(x) * math.cos(x))
    elif derivative_order == 2:
        return (2 * (math.sin(x)) ** 2 - 2 * (math.cos(x)) ** 2 - 1/2)


def newton(a, b, e):
    def cycle(b, k):
        x = b - f(b, 0) / f(b, 1)
        k += 1
        if abs(x - b) < e:
            return x, k
        else:
            b = x
            result = cycle(b, k)
        return result

    if f(a, 0) * f(b, 0) < 0:
        k = 0
        if abs(b - a) < e:
            x = (a + b) / 2
            return x, k
        else:
            if f(b, 0) * f(b, 2) > 0:
                result = cycle(b, k)
            else:
                z = b
                b = a
                a = z
                result = cycle(b, k)
        return result
    else:
        return 'error'
