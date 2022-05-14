#주민등록번호 String을 선언
personalNum = "19930601-1668479"
#주민번호의 성별부분 1부분을 출력
print('성별 :' + personalNum[7]) #스트링 배열의 0부터의 7번째를 의미하는거같다.
print("출생년도는 :" + personalNum[0:4]) # :은 왼쪽부터 오른쪽 까지를 뜻한다 오른쪽 숫자는 미만이다. 시작은 0번부터

print(personalNum[:8]) #왼쪽을 비워두면 처음부터라는 뜻이다.
print(personalNum[9:]) #9부터 끝까지라는 뜻이다.

#맨 뒤에서 7번째부터 끝까지
print(personalNum[-7:])
 
#문자 처리 함수
name = 'Lee Ssun Heum'
print(name.lower()) #모든 글자를 소문자로 출력하겠다. .lower()
print(name.upper()) #모든 글자를 대문자로 출력하겠다. .upper() 
print(name[0].isupper()) #[0]번째의 문자가 대문자입니까 하고 물어보는 코드 [].isupper() == true or false
print(name[1].islower()) #[1]번째의 문자가 소문자 입니까 하고 물어보는 코드 [].islower() == true or false
print(len(name)) #해당 변수의 길이가(문자갯수)가 얼마입니까 자바의 .length() 와 같다. .len(변수)
print(name.replace("Lee", "Kim")) #해당 변수안의 어떤글자를 어떤글자로바꾸겠다 .place("123","456")

index = name.index("e") #name 이란 변수에서 e가 어디에 들어있는가? *첫번째 e를 찾음
print(index) #첫번재 e인 1번을 찾음
index = name.index("e", index + 1) # index 는 위의 e부분(0)번째 다음(+1)부터 찾음
print(index) #첫번째 e 다음 두번째 e
index = name.index("e", index + 1) 
print(index) #마지막 인덱스 ([2]번) 다음부터 찾음 == 10번째

#.find()라는 함수를 사용하여도 찾을 수 있다.
print(name.find("Ssun"))
print(name.index("Ssun"))
#다만 .find()와 .index()가 비슷하게 글자를 찾을 수 있지만 차이점은 찾는값이 없는경우 find 는 -1이란 값을 반환하고 index()는 오류를 유발한다

print(name.find('Moon')) #== -1
#print(name.find("Moon")) #== error

#count() 는 사용된 총 갯수를 세어준다.
print(name.count("e")) #== 3개