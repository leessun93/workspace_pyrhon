# for문

#range() 어디부터~ 어디까지
for waiting_no in range(1, 21): # == 1번부터 21미만까지
    print('대기번호 :{0}번 입니다.' .format(waiting_no))

#커피 완성 안내문
starbucks = ["김갑순", "최칠복", "강명자", "이복자", "최동남"]
for customer in starbucks :
    print("{0}손님 커피 나오셨습니다." .format(customer))

#while
customer = '토르'
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요" .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# 조건이 맞을경우 while문 탈출
#손님 이름이 김칠복일경우 while문을 멈추게하자
customer = "김칠복"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요? >")



#continue == 계속해라
absent = [2, 5, 11, 17]
no_book = [3, 19]
rude = [10]
for student in range(1, 21) : #1~20
    if student in absent :
        continue #계속해서 진행하라
    elif student in no_book :
        print("{0}번은 교무실로 가서 손들고 서있어" .format(student))
    elif student in rude :
        print("{0}번 이런 어린x의 xx 너 따라와임마" .format(student))
        break #멈춘다.
    print("{0}아 계속해서 읽어봐!" .format(student))

# 한줄 주석
#출석번호가 12345일때 전부 100을 붙여서 101 102 103 등등으로 출력하라
student = [1,2,3,4,5]
student = [i + 100 for i in student] #배열에서 포문으로 값을 더했다(?)
print(student)

#학생의 이름을 길이로 변환 len
student = ["ironman", "thor", "big_thor", "sall_thor"]
student = [len(i) for i in student]
print(student)

#학생의 이름을 대문자로 변환 .apper
student = ["ironman", "thor", "big_thor", "sall_thor"]
student = [i.upper() for i in student]
print(student)


