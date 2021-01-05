import random

guess_number = random.randint(1, 10)
count = 0

while True:
    user_num = int(input())
    if guess_number != user_num:
        count += 1
        if guess_number > user_num:
            print('숫자가 너무 작습니다.')
        elif guess_number < user_num:
            print('숫자가 너무 큽니다.')
    else:
        break

print("정답:", user_num,"\n시도:", count)

