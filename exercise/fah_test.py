# 2. import 모듈명
import exercise.faherenheit as fah


# 3. from 절에다가 모듈명을 쓰고 import절에 함수명을 적어준 케이스
# from exercise.faherenheit import c_to_f



c1 = float(input())

print(round(fah.c_to_f(c1), 2))

print('{:.2f}'.format(fah.c_to_f(c1)))

print(fah.sayhello('dkdk'))