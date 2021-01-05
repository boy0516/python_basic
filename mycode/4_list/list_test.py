'''
list 타입을 선언하고 list의 엘리먼트를 추가, 삭제 등등
'''


num_list = [6, 2, 3, 7, 5]
num_list2 = [10, 20, 30, 40, 50]

print(type(num_list), num_list)

print(num_list[0], num_list[0:3], num_list[3:])

for num, num2 in enumerate(num_list):
    print(num, num2)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)
print(str_list[1], str_list[2:4])

for num, num2 in enumerate(str_list):
    print(num,num2)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix),mix)

str_list[1]=  1

print(str_list)

str_list.append('co')
str_list.insert(1,'dudu')
print(str_list)

my_list = list('python')
print(type(my_list), my_list)

my_list2 = 'Hello, python'.split(',')
print(my_list2)

# packing 과 unpacking
# packing
my_list = ['aa', 'bb']

# unpacking
str1, str2 = ['cc', 'dd']

print(str1)
print(str2)

my_list3