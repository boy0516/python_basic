# 선수명, 선수 포지션, 선수 등번호
names = ['철수', '영이', '바둑이']
positions = ['DF', 'MF', 'GK']
back_numbers =[5, 10, 20]

# class 없이 여러병의 선수 정보를 2차원 배열에 저장하기

for na, po, ba in zip(names,positions,back_numbers):
    print(na, po, ba)

players =[[name,position,back_number] for name, position, back_number in zip(names, positions,back_numbers)]
print(players)
player1 = players[0]
print(player1)
#from 패키지명.모듈명 import 클래스명 or 함수명
from mycode.oop.python_class import SoccerPlayer

player = SoccerPlayer('dooly', 'MF', 10)
print(player)
players_obj =[SoccerPlayer(name,position,back_number) for name, position, back_number in zip(names, positions,back_numbers)]

player1 = players_obj[0]
player1.change_back_number(30)
# back_number 변경
print(player1)