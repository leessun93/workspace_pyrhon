#list

subway = [1, 2 ,3]
print(subway)

subway = ['박명수', '하하', '유재석', '정형돈']
#유재석은 몇번째 배열인가
print(subway.index("유재석")) #0,1,2 3번째인 2번배열에 들어있다.

#배열 추가
subway.append("노홍철") # .append는 항상 맨 뒤에
print(subway)

#중간 삽입
subway.insert(1, "길") #1번배열에 길을 추가하겠다.
print(subway)

#맨뒤에부터 꺼냄 (삭제라고 하기엔 좀 다름 이상함)
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

#count 도 사용가능
subway.append("유재석")

subway.append("유재석")

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#배열 정렬
num_list = [3,4,2,6,7,2,788]
num_list.sort()
print(num_list)
#배열 정렬 순서 뒤집기
num_list.reverse()
print(num_list)
#배열 모두 지우기
num_list.clear()
print(num_list)

#배열끼리 합치기
num_list = [3,4,2,6,7,2,788]
subway.extend(num_list)
print(subway)