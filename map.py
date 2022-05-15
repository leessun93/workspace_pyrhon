# map 과 같은개념인 키 값 키 값이다
cabinet = {1: "유재석" , 2 :123123, 3 : 5}
print(cabinet[1])
print(cabinet[2])

#get , []

print(cabinet.get(3)) #3이라는 키 값을 가져오겠다는뜻이다.

#print(cabinet[5]) #이 경우는 5라는 키값을 요청하지만 없기떄문에 에러가난다.
print(cabinet.get(5)) # 반면 이경우는 없는값이지만 none이라는 값을 받고 진행이 가능하다

print(cabinet.get(5, "사용가능")) #이경우 5라는 값이 없을때는 사용가능이라고 표기하도록 none값을 바꿔서 표현해준다.


#맵 확인 하는법 키 in 변수
print(5 in cabinet) #== False
print(3 in cabinet) #== True

#새로 추가하기 & 업데이트하기

cabinet[1] = "admin" #케비넷 [키] 의 값은 뭐다 하고 새로 덮어씌울쑤도있고 키값이 새 값이라면 추가되기도한다.
cabinet["password"] = "admingoodgoodgood" #키 값은 string도 가능하다.

print(cabinet)

#지우기
del cabinet[2] #2라는 키값을 가진 값을 지우겠다.
print(cabinet)

#key 들만 출력하기

print(cabinet.keys())

#value 들만 출력하기
print(cabinet.values())

#key, value를 같이 쌍으로 출력하기
print(cabinet.items())

#map 지우기
cabinet.clear()
print(cabinet)
#---------------------------------------------------------------------------------

#튜플 이게 뭔지 아직은 잘 모르겠다. 리스트보다 빠른 방식이라고 한다.

menu = ("돈까스","치즈까스") #한번 선언하면 추가 삭제등이 불가능하다
print(menu[0])
print(menu[1]) #인덱스 값으로 호출이 가능하다.

#한번에 여러변수와 값 적용
(name, age, hobby) = ("leeSsun", 30, "hellchang")
print(name, age, hobby)

#-------------------------------------------------------------------------------
#set 집합
#중복안됨, 순서 없음
my_set = {1,2,3,3,3,3}
print(my_set) #중복되는 3들은 3하나만 출력됨! 중복x

java = {"유재석","박명수","정형돈"} 
python = set(["유재석", "정준하", "전진"]) #두가지 방법으로 set할 수 있다.
#교집합 자바와 파이썬을 모두할 수 있는사람은?
print(java & python)
print(java.intersection(python)) #둘다 교집합이다. 둘 다 할 수 잇는사람

#합집합 자바를 할 수 있거나 파이썬을 할 수 있는 사람은? 나 이선흠이올시다.
print(java | python)
print(java.union(python)) # 둘중 하나라도 할 수 있는사람 따라서 전부 (중복값은 합쳐서 나타내준다, 순서는 보장되어지지 않는다)

#차집합 자바는 할 수있지만 파이썬은 못하는 사람은?
print(java - python)
print(java.difference(python))

#파이썬을 할 수 있는사람이 추가됨
python.add("정형돈")
print(python) #파이썬에 정형돈이 추가됨

#자바를 할 수 있는사람을 뺌
java.remove("박명수")
print(java) #자바에 박명수가 빠짐

#---------------------------------------------------------------------------------

#자료 구조의 변경   (형변환)

#커피숍
menu = {"커피","우유","쥬스"}
print(menu, type(menu)) #set 클래스로 표기된다

menu = list(menu)
print(menu, type(menu)) #list 클래스로 표기된다

menu = tuple(menu)
print(menu, type(menu)) #tuple 클래스로 표기된다

#결론 {} = set, [] = list, () = tuple