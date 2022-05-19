#모듈 java에서 클래스 따로 만들어서 사용하는것 같다.
#import class이름 만 하면 뷰에서 임포트가 가능하다

#일반 가격
def price(people):
    print("{}명의 가격은 {}원 입니다." .format(people, people * 10000))

#조조 할인 가격
def MorningPrice(people):
    print("{}명의 조조 할인 가격은 {}원 입니다." .format(people, people * 6000))

#군인 할인 가격
def SoldierPrice(people):
    print("{}명의 군인 할인 가격은 {}원 입니다." .format(people, people * 4000))