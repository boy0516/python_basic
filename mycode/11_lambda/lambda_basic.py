def add(x, y):
    return x+y

print(add(12, 13))

add2 = lambda x, y: x + y

print(add2(10, 22))

print((lambda x,y:x+y)(10, 12))

print((lambda x: x**2)(10))

#map(함수, 리스트)함수

double_val = lambda x: x ** 2
print(double_val(2))
my_list = [1, 2, 3, 4, 5]
my_list2 = [10, 20, 30, 40, 50]
result = map(double_val, my_list)
print(type(result), result)
result = list(map(double_val, my_list))
print(result)

result = list(map(lambda x: x ** 2, my_list))
print(result)
# my_list를 순회 (iterate) 하면서 값을 제곱값을 반환하는 함수를 호출한다.


result = list(map(lambda x, y : x+y, my_list, my_list2))
print(result)

# 짝수만 제곱하는 함수
double_even = lambda x: x**2 if x %2 == 0 else x
print(double_even(4), double_even(5))
print(list(map(double_even, my_list)))


'''
reduce() 함수
'''

from functools import reduce

add2 = lambda x, y: x + y
print(add2(10, 20))

result = reduce(add2, my_list)
print(result)
result = reduce(lambda prev, curr: prev + curr, my_list)

result_str = reduce(lambda prev, curr: prev +curr, my_list)
print(result_str)

my_len = lambda my_str: len(my_str) > 6

print(my_len('hello')), my_len('mypython')

my_list_str = ['hello', 'mypython', 'machine', 'deep', 'datascience']

#6글자 이상이 문자열만 리스트에 저장하기
result = filter(my_len, my_list_str)

print(result)
print(list(result))
