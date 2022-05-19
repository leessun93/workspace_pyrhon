#예외처리 java에서는 IOEexcption try{}catch(){}
from logging import exception


try:
    print("나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
#파이썬에서는 try: excpt 코드:
except ValueError: #잘못된 벨류를 입력하였다 예를들어 숫자인데 String을 입력한경우
    print("에라! 잘못된 값을 입력 하였습니다.")
except ZeroDivisionError as err: #0으로 나눌수 없다!
    print(err)
except: #나머지 예외처리들을 넣어주나보다
    print("알수없는 예외가 발생하였습니다.")

#의도적으로 에러 만들기

try:
    print("한자리 숫자 전용 나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: #만약 1번 2번 받은값이 2자리 이상일경우
        raise ValueError #위의 조건이 안맞을경우 벨류에러를 일으킨다 
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러 잘못된 값을 입력하였습니다.")

#사용자 정의 예외처리
class bigNumberError(Exception): #Excption 오브젝트 클래스를 상속받아서 재 정의한듯 싶다.
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한자리 숫자 전용 나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: #만약 {1번 2번 받은값이 2자리 이상일경우
        raise bigNumberError("입력값 : {0}, {1}" .format(num1, num2)) #위의 조건이 안맞을경우 벨류에러를 일으킨다 
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러 잘못된 값을 입력하였습니다.")
except bigNumberError as err:
    print("내가 정의한 에러입니다. 하핫")
    print(err)

#finally
finally: #예외처리를 잘 수행했던 안했던 마지막 안내구문
    print("계산기를 이용해주셔서 감사합니다.")


#치킨 포스기 완성해보자

class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]" .format(chicken))
        order = int(input("치킨 몇 마리 주문 하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력 하였습니다.")
    except SoldOutError:
        print("재고가 모두 소진되어 오늘 장사 접습니다 수고")
        break