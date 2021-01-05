
'''
나이= 현재 년도 - 태어난 년도 +1
태어난 년도를 입력 받음 input()

from 모듈명 import
'''

from datetime import datetime as dt
#현재년도
current_year = dt.today().year
print(current_year)

bornyear = int(input())

age = current_year - bornyear + 1

if age>=17 and age<20:
    print("고등학생")
elif age>=20 and age<27:
    print("대학생")
else:
    print("학생이 아닙니다")
