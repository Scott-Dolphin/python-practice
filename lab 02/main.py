from header import *

list01 = [1,2,3,4,5,8,2,4,23,77,2,1,4,3,5]
list02 = [10,20,30,40,50,]
list03 = [1,2,3,4,5,6,7]
list04 = [-2,4,5,6]
test_String = 'hello'

# testing example 1
print('testing with (1, 2, 3):              expected: 3      returned:', max3(1, 2, 3))
print('testing with (1, 3, 2):              expected: 4      returned:', max3(1,4,2))
print('testing with (5, 2, 1):              expected: 5      returned:',max3(5,2,1))


print('testing with large sample:           expected: 77     returned:', list_max(list01))

#testing example 2
print('testing with large sample:           expected: 144    returned:', list_sum(list01))
print('testing with small sample:           expected: 150    returned:', list_sum(list02))

# testing example 3
print('testing with small sample:           expected: -240   returned:', list_product(list03))
print('testing with small sample:           expected: 5040   returned:', list_product(list04))

# testing example 4
print('testing with "hello":                expected: olleh  returned:', string_reverse(test_String))