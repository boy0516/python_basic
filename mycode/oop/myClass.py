#클래스 선언
#class MyClass extends Object{}, class MyClass{} - java

class MyClass(object):
    #constructor 생성자 선언
    def __init__(self):
        # attribute(속성) 초기화
        self.num = 100
        # private 속성
        self.__name = 'dooly'

    # method(행위) 선언
    def read_number(self):
        print(self.num)
    #부모 클래스(object)가 가진 __str__메서드를 재정의 하였슴
    def __str__(self):
        return f'MyClass의 속성 {str(self.num)}'

    # getter method
    @property     #프로퍼티를 붙이면 메서드지만 ()없이 변수처럼 써도 된다.
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:    # 이렇게 셋터에 조건을 줘서 외부에서 함부로 값을 변경하지 못하게 보호할 수 있다.
            self.__name = new_name

myobj1 = MyClass()
print(myobj1, type(myobj1))

print(myobj1, type(myobj1))

# getter method 호출
print(myobj1.name)

# setter method 호출
myobj1.name = '길동'
print(myobj1.name)

print(myobj1.read_number())