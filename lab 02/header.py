# 1. find the max of 3 numbers
def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

def list_max(list):
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]

    return max

# 2. Return sum of a list
def list_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

# 3. return product of a list
def list_product(list):
    product = 1
    for i in range(len(list)):
        product *= list[i]
    return product

# 4. reverse a string
def string_reverse(w):
    result = ''
    i = len(w)
    while i > 0:
        result += w[i - 1]
        i -= 1
    
    return result

# 5. calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result