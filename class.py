# 클래스 생성 java에서는 public class className{} 으로 정의했다.
#일반유닛
class Unit: #클래스 이름 
    def __init__(self, name, hp, damage): #인스턴스로 생성할때 self는 빼고 써야한다 self는 java에서 this와 같은것 같다.
        self.name = name                  #__init__은 생성자이다 자바에서 생성자는 public 클래스이름(필드, 필드, 필드)였다.
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#맴버 변수
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage)) #이런식으로 겟터를 별 선언 없이도 사용가능하다.

wraith2 = Unit("레이스2", 80, 5)
wraith2.clocking = True #이런식으로 java에서는 상상도못할 외부에서 메소드를 생성해서 넣어줄 수 있다. 확장한 객체에서만 적용된다

if wraith2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다." .format(wraith2.name))


#공격 유닛
class AttackUnit: #한 파일 안에 여러 클래스를 정의할 수 있나보다. 이상하다
    def __init__(self, name, hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 한 클래스 안에서 정의된 self 안의 변수들은 공유하나보다
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage)) #location은 self를 안썼으니 전달받아야한다

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))


#실행해보기 파이어벳
firebat1 = AttackUnit("파이어벳", 50, 16)
firebat1.attack("5시")

#공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
