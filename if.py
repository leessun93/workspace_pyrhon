# if 문
# 자바에서의 if(){
#           }else if(){
#           }else{
#           } 와 같다
weather = '비'

if weather == '비' or weather == '눈' :         #파이썬에서는 or라고 조건을 두개를 걸 수 있다. 그냥 두번쓰지 참
    print('우산을 챙기세요')
elif weather == '미세먼지' :
    print('마스크를 챙기세요')
else :
    print('화창한 날씨입니다.')
    
#90점 이상이면 a등급 80점 이상이면 b등급 70점이면 c등급 나머지는 낙제를 출력하시오

grade = int(input('점수는 몇점입니까? >'))   #input은 sc.nextInt와 같다 그리고 인풋은 string으로 받기때문에 int로 형변환을 해주어야한다

if 90<= grade < 100 :
    print('A등급입니다.')
elif 80<= grade < 90 :
    print('B등급입니다.')
elif 70<= grade <80 :
    print('C등급입니다.')
else :
    print('글러먹었쓰 집에 가임마!')

# -----------------------------------------------------------------------------------------------
