# 1. find the max of 3 numbers
def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

