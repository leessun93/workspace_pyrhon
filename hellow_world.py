print("helloWorld")
# 이것이 파이썬의 한줄 주석
''' 큰따옴표 3개나
    작은따옴표 3개로 여러줄 주석 사용가능 귀찬
'''
# 파이썬의 터미널이란곳은 자바의 콘솔부분과 역할이 같다.
# 디버그를 눌러 위에 초록색 세모 버튼을 눌러도 사용이 가능하다
# 파이썬은 ;로 문장을 닫아주지않는다 신기방기쓰

# 자료형
# 1.인티저 소수점 음수 양수 다 그냥 사용됨
print(3.14)
# 2.String '' "" 를 사용
print('하이')
# 특이한점은 String에 *를 사용가능
print('야쓰'*10)
#3.boolean 사용가능
print(5>10) #거짓

print(True) #불린 대문자로 해서 사용가능 파란색으로 출력된다 주의할것 첫글자 대문자
print(False) #거짓
#특이한건 != 기능이다
print(not True)
print(not False) #이런식으로 표현 가능하다





# 변수 선언
name = "리썬" # == String
age = 30 # == int
result = 1998 >= 1993


#스트링이 아닌 다른 자료형은 변수 앞에str()로 형변환을 해주어야한다 
#print('제 이름은' + name +'입니다 나이는'+ age+'이구요 생년월일은' + result+'입니다.')
#따라서 위의 변수들 앞에 str을 붙여주어야한다.
print('제 이름은' + name +'입니다 나이는'+ str(age)+'이구요 생년월일은 1993이' + str(result)+'입니다.')

#함수는 중복선언이 가능하다

name = "이선흠" #앞의 리썬이 이선흠으로 덮어씌워진다

print(name)

#연산자
#+-/* 다 같다 하나 특이한점
print(5**3) #**를 두개쓰면 제곱이된다. 5의 3제곱
print(13//3) #나머지를 구하는 %와 반대로 몫을 구한다. 답은 4

#비교

#둘다 맞으면 참이다.
print((3>0) and (5<10))
print((3>1) & (7<12))
#둘중 하나만 맞아도 참이다.
print((3>0) or (5>6))
print((3>0) | (5>6))

#파이썬의 숫자 처리 함수
#absolute 절대값
print(abs(-12)) # ==12
#power 파워
print(pow(4,2)) #== 4의 2승 16
#max 최대값 둘중 더 큰수를 출력
print(max(20, 29)) #==29
#min 최소값 둘중 더 작은수 를 출력
print(min(21, 9)) #== 9
#round 반올림
print(round(3.14)) #==3
print(round(6.9)) #==7

#파이썬의 매스 클래스를 모두(*) 임포트 하겠다
#아래의 수식들은 임포트 후 사용 가능
from math import *
print(floor(4.99)) #내림 ==4
print(ceil(3.14)) #올림 ==4
print(sqrt(16)) #제곱근 == 4


#파이썬의 랜덤 클래스를 모두(*) 임포트 하겠다
from random import *
print(random()) #0.0 이상 1.0 미만의 랜덤의 숫자를 출력해준다
print(random() * 10) #0.0 부터 10.0 미만의 임의값을 출력하겠다
print(int(random() * 10)) #0부터 10까지 int 인티저 즉 정수값만 출력하겠다.
print(int(random() * 10) +1) # 1부터 10까지의 정수 값만 출력하겠다.

#로또 만들기
print("--------------------------------------------------")
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
#파이썬에서는 더 쉬운 방법을 제공한다
#randrange 미만
print("--------------------------------------------------")
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
print(randrange(1 , 46)) #1부터 46미만 ==45 까지의 숫자를 랜덤 제공한다 
#randint 이하
print("--------------------------------------------------")
print(randint(1,45)) #1부터 45 이하의 숫자를 출력
print(randint(1,45)) #1부터 45 이하의 숫자를 출력
print(randint(1,45)) #1부터 45 이하의 숫자를 출력
print(randint(1,45)) #1부터 45 이하의 숫자를 출력
print(randint(1,45)) #1부터 45 이하의 숫자를 출력
print(randint(1,45)) #1부터 45 이하의 숫자를 출력

#스터디 날짜는 매월 x 일로 선정되었습니다 (28일까지 1 2 3일은 제외 숫자를 출력하시오)

date = randint(3, 28)
print('스터디 날짜는 매월'+ str(date) +'일로 선정되었습니다.')

#String

str1 = '안녕하세요'
print(str1)
str2 = "'반갑습니다'"
print(str2)
str3 =  """
        저는 리썬입니다
        별명은 이선흠이지요
        """
print(str3) # """부분과 아래 탭부분 전부 들어간다

#U 확인용