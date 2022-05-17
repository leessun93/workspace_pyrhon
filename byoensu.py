#지역변수와 전역변수 == 사용하고 사라지는 변수와 전체적으로 적용되는 변수 global

gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}" .format(gun))

print("전체 총 : {0}" .format(gun))
checkpoint(2) #2명이 경계근무를 나감
print("남은 총 : {0}" .format(gun))


#남자와 여자의 표준키를 구하는 함수를 만들어라 남자는 키*키*22 여자는 키*키*21

def avgHeight(gender, height):
    if gender == 'man':
        return height*height*22
    elif gender == 'woman':
        return height*height*21

print(round(avgHeight('man', 1.77), 2))
