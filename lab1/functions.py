import math


def linear_algorithm(b, c):
    y1_part1 = (b * math.sqrt(c)) / (2**b)
    y1_part2 = (c * math.sqrt(b)) / (2**c)
    y1_final = y1_part1 - y1_part2
    return y1_final


def branched_algorithm(a, b, x):
    if x > 0:
        y2_part1 = a * (x**3)
        y2_part2 = b * (x**2)
        y2_final = y2_part1 - y2_part2
    else:
        y2_part1 = b * (x**3)
        y2_part2 = a * (x**2)
        y2_final = y2_part1 + y2_part2
    return y2_final


def cyclic_algorithm(j, i, n1, n2):
    y3_part1 = None
    y3_part2 = 0
    while j <= n1:
        if y3_part1 is None:
            y3_part1 = math.factorial(j)
        else:
            y3_part1 *= math.factorial(j)
        j += 1
    while i <= n2:
        y3_part2 += math.factorial(i)
        i += 1
    y3_final = y3_part1 - y3_part2
    return y3_final
