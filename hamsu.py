#함수
#자바에서는 public int result(int i){ 
#          return : 1;
#          } 이렇게 사용하였다.

from typing_extensions import get_overloads


def open_account():
    print("새로운 계정이 생성되었습니다.")

# 실행은
open_account()

#입 출금
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금금액보다 같거나 커야만 출력이되게한다
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance - money))
        return balance - money
    else : #잔액이 출금금액보다 작다면 출금을 막는다.
        print("출금이 취소되었습니다. 잔액은 {0}원 입니다." .format(balance))
        return balance

#수수료
def whitdraw_night(balance, money): #밤에 출금
    commission = balance*0.01 #수수료는 예금의 1프로
    return commission, balance - money - commission #수수료와 잔액값 이렇게 여러 값을 리턴 할 수 있다.




balance = 0
balance = deposit(balance, 10000)
print(balance)

balance = withdraw(balance, 200)
print(balance)

commission, balance = whitdraw_night(balance, 5000)
print("수수료 {0}원 이며, 잔액은 {1}원 남았습니다. " .format(commission, balance))


#함수 호출
def profile(name, age, lang):
    print("이름은 {0} 나이는 {1} 언어는 {2}" .format(name, age, lang))

profile("박명수", 30 , "java") #순서대로 값을 넣어주면 실행되고
profile(age=40, name="유재석", lang="pythone") #순서가 바뀌어도 변수를 잘 맞춰주면 실행된다.


#가변인자
#갯수가 정해지지않은 값이 있을때 유동적으로 갯수를 넣어야할때
def profile(name, age, *lang):
    print("이름은 {0} 이고 나이는{1} 입니다." .format(name, age), end=" ")   #ende(" ") 는 줄바꿈을 하지않고 이어서 붙이겠다는뜻이다
    for language in lang:
        print(language, end=" ")
    print()

profile("아이언맨", 50, "java","python", "c++", "c", "javascript", "jQuery", "SQL")
profile("터미네이터", 69, "english")