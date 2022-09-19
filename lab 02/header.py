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
    product = 0
    for i in range(len(list)):
        product += list[i]
    return sum

# 4. reverse a string
def string_reverse(w):
    result = ''
    for i in range(len(w)):
        result.insert(0, w[i])
    return result