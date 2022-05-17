# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고있삽니당")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#문제 매 주차 보고서를 만들어라

#for문으로 돌리고 안에 파일 스트림 넣고 내용에 숫자넣고


for index in range(1,51):
    bogo = open(str(index)+"주차.txt", "w", encoding="utf8" )
    bogo.write("- {0} 주간 업무보고-" .format(index))
    bogo.write("\n부서 :")
    bogo.write("\n이름 :")
    bogo.write("\n업무 요약 :")
    bogo.close()