def list_multiples(n):
    multiples = []
    for i in range(1, n + 1):
        if n % i == 0:
            multiples.append(i)
    return multiples

def gcd(j, k):
    number_1 = list_multiples(j)
    number_2 = list_multiples(k)
    greatest = 0

    for i in number_1:
        if (i in number_2) and (i >=0):
            greatest = i
    return greatest

def lcm(j, k):
    numerator = abs(j * k)

    return numerator / gcd(j, k)