#상속에 대해서
#일반유닛
class Unit: #클래스 이름 
    def __init__(self, name, hp,): #기본적인 부모클래스이다.
        self.name = name                  
        self.hp = hp


#공격 유닛
class AttackUnit(Unit): #상속받을 자녀 클래스이다 상속하려면 클래스이름 옆에 (부모클래스이름) 을 넣어주어야한다.
    def __init__(self, name, hp,damage):
        Unit.__init__(self, name, hp) #생성자를 생성자 안에 그냥 불러와버린다 java로 치면 Super()같은 개념인가보다
        self.damage = damage

    def attack(self, location): # 한 클래스 안에서 정의된 self 안의 변수들은 공유하나보다
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage)) #location은 self를 안썼으니 전달받아야한다

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))


#다중상속  자바에서는 다중상속을 지원하지 않았다. 이번에 처음쓰는개념 긴장된다
class flyable:
    def __init__(self, flying_speed): #__init__ 은 생성자이다. 잊지말자
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날라갑니다. [속도 : {2}]" .format(name, location, self.flying_speed))

#드디어 다중상속 시작
class FlyableAttackUnit(AttackUnit, flyable): #AttackUnit 은 이미 unit을 상속받은상태이고 이것과 플라이어블 두개의 부모를 가진생성자이다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)

#사용해보자 발키리를 만들자
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) #AttackUnit 부모클래스에서 name hp damage flying_speed 4개를 넣었었다.
valkyrie.fly(valkyrie.name, "3시") #flyable 부모클래스에서 fly 메소드를 사용했다.