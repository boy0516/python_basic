'''
yesterday.txt 파일을 읽어서
YESTERDAY 라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday 라는 단어가 몇번 나왔는지 yesterday_lyric.count('Yesterday')
yesterday 라는 단어가 몇번 나왔는지 yesterday_lyric.count('yesterday')
숙제
'''

f = open("yesterday.txt", 'r')
data = f.read()

n1 = data.upper().count('YESTERDAY')
n2 = data.count('Yesterday')
n3 = data.count('yesterday')

print(n1, n2, n3)

def file_read(file_name):
    with open('yesterday.txt', 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric