from header import *
import random
test =  10

#Leap year
print('test is a leap year:', checkYear(test))

#quadratic equation
print('roots for (2x^2 - 11x + 5):\n    ', findRoots(2, -11, 5))
print('roots for (x^2 -x -2):\n     ', findRoots(1, -1, -2))

#prime number
print(test, 'is a prime number:', checkPrime(test))

#check armstrong
print(test, 'is an armstrong number:', checkArmstrong(test)) #fixme

#convert miles to km
print('50 miles is', milesToKm(50), 'km')

#convert fahrenheit to celsius
print('32f in c is', fahToCel(32))

#print the fibonacci sum of the first n terms
print(Fibonacci(10))

#print random number
print('printing random number;', random.randrange(100))