#연산자 오버로딩 
#상속에 대해서
#일반유닛
class Unit: #클래스 이름 
    def __init__(self, name, hp, speed): #기본적인 부모클래스이다.
        self.name = name                  
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]" .format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit): #상속받을 자녀 클래스이다 상속하려면 클래스이름 옆에 (부모클래스이름) 을 넣어주어야한다.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #생성자를 생성자 안에 그냥 불러와버린다 java로 치면 Super()같은 개념인가보다
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
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 == 0으로 처리
        flyable.__init__(self, flying_speed)

    def move(self, location): #부모, unit 클래스의 move를 그대로
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#오버로딩을 설명하기위에 기본 유닛에도 speed를 추가해보겠다.

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시") 
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") #배틀도 무브라는 부모 메소드를 그대로 불러와서 재정의하여 사용했다.


#pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass #아무것도 안하고 일단은 넘어간다 이게 뭔소리야

#서플라이디폿으르 만들어보자
supply_depot = BuildingUnit("서플라이디폿", 500, "7시")

#pass 활용해보기

# def game_Start():
#     print("[게임이 시작되었습니다.]")

# def game_Over():
#     pass

# game_Start()

# game_Over() 

#Super() 이건 자바랑 똑같나보다
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
    #def __init__(self, name, hp, 0): #전에 쓴건데 슈퍼로도 쓸수 있어서 주석처리 하였다.
        #pass
        super().__init__(name, hp, 0) #슈퍼를 사용하면 self를 안 써도 된다.
        self.location = location