from math import sqrt
from math import pow
from math import log10

# mod 4, if it's zero, it should be a leap year
def checkYear(y):
    if y % 4 == 0:
        return True
    else:
        return False


def findRoots(a, b, c):

    try:
                                                                # note: function was split into the numberator and denominator, not sure why
                                                                # doing so fixed the error but I'll take it
        positive = ((b * -1) + sqrt(pow(b,2) - (4 * a * c)))
        negative = ((b * -1) - sqrt(pow(b,2) - (4 * a * c)))
        answer = (positive / (2 * a), negative / (2 * a))
        return answer
    except:
        return 'domain error'
    
def checkPrime(n):
    if (n > 1):
        for i in range(2, n):
            if(n % i == 0):
                return False
    return True

# not including negative numbers
def countDigits(n):
    if n > 0:
        return int(log10(n)) + 1
    elif n ==0:
        return 1

def checkArmstrong(n): #error resolved, stores original parameter as n_temp and then manipulated
    n_temp = n
    digits = countDigits(n)
    answer = 0
    for i in range(digits):
        answer += pow(n_temp % 10, digits)
        n_temp = int(n_temp / 10)
    return n == answer


def milesToKm(miles):
    return miles * 1.609347

def fahToCel(f):
    f -= 32
    f *= 5
    f /= 9
    return f

#fixme: potential logic error
def recurFibonacci(n):
    if n < 1:
        return n
    else:
        return(recurFibonacci(n-1) + recurFibonacci(n-2))

#fixme: potential logic error: throwing negative number?
def printFibo(n):
    if n <= 0:
        print('please enter a positive integer')
    else:
        print('fibonacci sequence up to', n)
        for i in range(n):
            print(recurFibonacci(i))