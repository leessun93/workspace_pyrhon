#다중상속의 문제점 첫번째 생성자만 호출된다.
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class Flyableunit(Unit, Flyable):
    def __init__(self):
        # super().__init__() #두개 이상의 부모 클래스를 상속받는경우 super()를 사용했을시 순서상의 맨 마지막에 상속받는 클래스에서만 init 함수가 호출이 된다
        Unit.__init__(self)
        Flyable.__init__(self) #이런식으로 두개를 초기화 해주어야한다
#드랍쉽
dropship = Flyableunit()