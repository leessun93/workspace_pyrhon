#sep == ,부분을 전부 뭘로 채워준다. end="" 는 문장의 끝에 뭘 넣어준다 
print("python","java", sep="!", end="*")
print("javaScript", "Oracle")

#표준 출력과 표준 에러 exception같은건가보다
# import sys
# print("python","java", file=sys.stdout)
# print("javaScript", "Oracle", file=sys.stderr)

scores = {"수학 :": 0, "영어 :": 50, "코딩 :": 100}
for subjact, score in scores.items(): #스코어라는 리스트의 키 값 두개를 섭젝 스코어 변수에 넘겨준다
    # print(subjact, score)
    print(subjact.ljust(8), score) #.ljust(int) == left정렬인데 8칸을 확보해달라
    print(subjact.rjust(8), score) #.rjust(int) == right정렬인데 8칸을 확보해달라

#은행 순번 대기표 ==.zfil(int)
#001, 002, 003 ...

for num in range(1, 21):
    print("대기순서 :" + str(num).zfill(3)) #3자리수를 쓰는데 남는공간을 0으로 채워주십시오 하는 코드

#--------------------------------------------------------------------------------------------------
#빈자리는 빈 공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보해서 출력해라
print("{0: >10}" .format(500)) # 0번쨰에: 여긴 빈공간으로 두고 >우측정렬 10개확보
#양수일때는 +로 표시 음수일때는 -로 표시
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500)) # >+10 을써주면 양수이거나 음수일때 항상 + - 를 출력해준다.
#왼쪽정렬하고 빈 공간을 _로 채워라
print("{0:_<10}" .format(500))
#3자리마다 콤마를 찍어달라
print("{0:,}" .format(100000000)) #왜 그냥 콤마는 3자리마다라고 미리 정해져있는거지?
#3자리마다 콤마를 찍어달라 그리고 + - 도 붙여달라
print("{0:+,}" .format(100000000)) #왜 그냥 콤마는 3자리마다라고 미리 정해져있는거지?
#3자리마다 콤마를 붙이고 부호도 붙이고 자릿수도 확보하고 돈이많으면 좋으니 빈공간에 ^도 붙여달라
print("{0:^<+30,}" .format(850000000000))
#소수점 출력 .f ==아마 자바 자료형의 float같다
print("{0:f}" .format(5/3))
#소수점 2째자리까지 출력 == .2f
print("{0:.2f}" .format(5/3))