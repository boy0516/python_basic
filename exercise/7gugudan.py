while True:

    print("구구단을 몇 단을 계산할까요(1~9)?")
    dan = int(input())

    if 1 <= dan <= 9:
        print("구구단", dan, "단을 계산합니다.")
        for i in range(1, 10):
            print(dan, "X", i, "=", dan * i)
    else:
        print("구구단 게임을 종료합니다.")
        break
