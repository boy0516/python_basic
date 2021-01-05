class SoccerPlayer(object):
    # 생성자 함수 - 객체 생성될때 호출됨
    def __init__(self, name, position, back_number=20):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    #객체 주소 대신에 원하는 다른 속성값을 반환해주는 메서드드
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center %s" % (self.name, self.position, self.back_number)


def main():
    jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
    print(jinhyun)

    print("현재 선수의 등번호는 :", jinhyun.back_number)
    jinhyun.change_back_number(5)
    print("현재 선수의 등번호는 :", jinhyun.back_number)

# 실행했을 경우에만 main()함수를 호출하라
#import 한 경우에는 main함수는 호촐되지 않는다.
if __name__ == "__main__":
    main()