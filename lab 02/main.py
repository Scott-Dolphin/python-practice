from header import *

list01 = [1,2,3,4,5,8,2,4,23,77,2,1,4,3,5]
list02 = [10,20,30,40,50,]
list03 = [1,2,3,4,5,6,7]
list04 = [-2,4,5,6]
test_String = 'hello'

# testing example 1
print('\n                                         ~~~EXAMPLE 1~~~')
print('01- testing with (1, 2, 3):              expected: 3                     returned:', max3(1, 2, 3))
print('02- testing with (1, 3, 2):              expected: 4                     returned:', max3(1,4,2))
print('03- testing with (5, 2, 1):              expected: 5                     returned:',max3(5,2,1))


print('04- testing with large sample:           expected: 77                    returned:', list_max(list01))

#testing example 2
print('\n                                         ~~~EXAMPLE 2~~~')
print('05- testing with large sample:           expected: 144                   returned:', list_sum(list01))
print('06- testing with small sample:           expected: 150                   returned:', list_sum(list02))

# testing example 3
print('\n                                         ~~~EXAMPLE 3~~~')
print('07- testing with small sample:           expected: -240                  returned:', list_product(list04))
print('08- testing with small sample:           expected: 5040                  returned:', list_product(list03))

# testing example 4
print('\n                                         ~~~EXAMPLE 4~~~')
print('09- testing with "hello":                expected: "olleh"               returned:', string_reverse(test_String))
print('10- testing with "happy go lucky"        expected: "ykcul og yppah"      returned:', string_reverse('happy go lucky'))

# testing example 5
print('\n                                         ~~~EXAMPLE 5~~~')
print('11- testing with 6:                      expected: 720                   returned:', factorial(6))
print('12- testing with 3:                      expected: 2                     returned:', factorial(2))
print('13- testing with 8:                      expected: 40320                 returned:', factorial(8))

