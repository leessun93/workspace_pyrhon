import pickle
profile_file = open("profile.pickle", "wb") #롸이트 바이너리 따로 인코딩 설정 필요x
profile = {"이름":"박명수", "나이":30, "취미":["축구","야구","롤"]}
print(profile)  #파일을 쓰기위한것 덤프, (프로필, 프로파일) 프로필의 정보를 프로파일에 넣겠다.
pickle.dump(profile, profile_file)

profile_file.close()


#읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()