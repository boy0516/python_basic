
# dict 타입
# dict(), {}

lang_dict ={}
lang_dict2 =dict()
print(type(lang_dict), type(lang_dict2))

lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[200] = '텐서플로'
lang_dict[300] = 'PyTorch'

print(lang_dict)


print('자바' in lang_dict.values()) #벨류 값이 있는지 찾는것

#zip() 함수

days = ['월요일', '화요일', '수요일']
fruits =['사과','바나나', '딸기']
coffees = ['아메리카노', '라떼','모카','믹스']

print(zip(days,fruits,coffees), type(zip(days,fruits,coffees)))

for day, fruit, coffee in zip(days,fruits,coffees):
    print(day, fruit, coffee)

print(dict(zip(days,fruits)))
print(list(zip(days,fruits)))

for value in list(zip(days,fruits)):
    print(value)

days_tuple = '월요일', '화요일', '수요일'
coffees_tuple = '아메리카노', '라떼','모카'
print(type(days_tuple))


#zip(), range() 함수는 iterable객체를 반환하기 때문에 값을 확인하려면 for in 구문 리스트를 이용한다.

