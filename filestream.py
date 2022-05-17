score_file = open("score.txt", "w", encoding="utf8") #open()을 통해야만 파일을 열 수 있고 , 경로, "w" 를 써주어야 쓰기목적이다라고 선언 
#encoding="utf8"은 한글 선언
print("수학 : 0", file=score_file)
print("영어 : 70", file=score_file)
score_file.close() #파일을 닫아야한다

score_file = open("score.txt", "a", encoding="utf8") #"a" 는 어펜드 이어서 쓰겠다는 소리다
score_file.write("과학 : 80")
score_file.write("\n대학 : 180")
score_file.close()


#읽어오기 Read = "r"
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

#한줄씩 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
score_file.close()


#몇줄인지 모를때 한줄씩 불러와서 와일문으로 전부 출력 그리고 값이 없다면 break
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() #
    if not line:
        break
    print(line, end="")
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장하여 for문으로 한줄씩 출력한다
for line in lines:
    print("=============")
    print(line, end="")
score_file.close()
