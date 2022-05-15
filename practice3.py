# 문자열 포멧
print("나는 %d 살입니다." %20) #%d %정수값 을 해서 int값을 넣을 수 있다.
print("나는 %s 를 좋아해ㅛ" %'피자') #%s %문자 해서 String값을 넣을 수 있다. 숫자도 거의 스트링으로 넣을 수 있다.
print("diablo 는 %c 로 시작해요" %'D') #%c %문자 로 char를 쓸수 있다.
print("저는 주로 %s 과 %s을 갑니다." %('탑', "정글")) #이런식으로 순서대로 두개도 넣을 수 있다.

# format
print("나는 {}를 주로하고 가끔{}도 합니다" .format('탱커', '서포터')) #{} 순서대로 .format() 안의 값들이 들어간다
print("나는 {1}를 주로하고 가끔{0}도 합니다" .format('탱커', '서포터'))#{} 안의 숫자 순서대로 format()안의 값들이 들어간다
print("나는 {line1}를 주로하고 가끔{line2}도 합니다" .format(line1 = '탱커', line2 ='서포터')) #변수로 선언해서 안에 변수 넣어주는것도 가능

#변수를 미리 선언해주는경우
line1='탱커'
line2='원딜'

print(f'나는 {line1} 를 주로 하지만 종종 {line2} 도 갑니다.') #변수를 미리 선언해줄경우 print 안의 문장 맨앞에 f를 붙여주어야 한다.


#탈출 문자
#\n 줄바꿈
print("안녕하세요 \n반갑습니다")
#' "를 사용하기위해선 문장 시작을 상반되는 따옴표로 시작하면 된다.
#다른 방법으로는 \' \"를 사용해주면 따옴표를 그대로 사용할 수 있다.
#\를 사용하기위해선 \\ 두번써주면 된다.
print("c:\\Users\\python\\workspace\\helloworld.py") #이런경우 사용한다.

# \r 커서를 맨 앞으로 이동
print('Red apple\rfine') #\r부분을 맨 앞으로 옮겨서 바꾼다는데 솔직히 잘 모르겠고 잘 안쓰이는거같다 이거 이해가 안간다
# \b 백스페이스  한글자 삭제
print('redd\b apple') #바로 뒤의 한글자를 지운다는데 이런걸 어디다 활용한다는거지 도대체 아마 부분 팔스인트 그런건가
# \t 텝
print('fine \t apple')

#사이트 주소를 입력하면 비밀번호를 자동으로 만들어주는 프로그램을 만들어라

site1 = 'http://naver.com'
# 규칙 1 http:// 부분 제외 = site1[7:] ==7번째부터 끝까지
# 처음 만나는 (.) 이후 부분은 제외 ==site1[:-4]
site1 = site1[7: -4]
print(site1)
print(str(site1[0: 3]) + str(len(site1)) + str(site1.count('e')) + '!' )

#정답

url = "http://naver.com"
modiUrl = url.replace("http://", "")
modiUrl = modiUrl[:modiUrl.index(".")]  #index .까지 찾겠습니다.
password = modiUrl[: 3] + str(len(modiUrl)) + str(modiUrl.count("e")) + '!'
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))


