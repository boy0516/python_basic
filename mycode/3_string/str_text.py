'''
문자열관련내용
'''

greet = 'Hello' * 4 + '\n'
end = 'good\'bye\''
end2 = "'got'"
print(greet + end + end2)

is_flag =False
my_str ='False'

greeting = 'hello world'

print('문자열 길이', len(greeting))
print('문자열 길이 {}, {}'.format(len(greeting), greeting[0]))
print('{1}')

#3.6 version 이후에 생긴것

print(f'문자열 길이 {len(greeting)}')

print(greeting, greeting[:])
print(greeting[::2]) #두칸씩 뛰어 넘음

print(greeting[::-1]) #역순으로 나열


word = 'Good manufacturing Practice Good'
print(word)
print(word.upper())
result = word.upper()
print(word, ' ', result)
print(f'소문자로 변환= {word.lower()}')
print(word.title())
print(word.find('m'))
print(word.rfind('m'))
print(word.count('m'))

word_list = word.split()
print(word_list)
word2='Good/manu/facturing/Practice/Good'
print(word2.split('/'))

for val in word:
    print(val, word.count(val))
    