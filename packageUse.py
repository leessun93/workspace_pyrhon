import travel.thailand #임포트 패키지점 클래스파일
trip_to = travel.thailand.ThailandPackage() #트립 투 = 패키지.파일.클래스
trip_to.detail()

from travel.thailand import ThailandPackage #프롬 패키지.파일 임포트 클래스
trip_to = ThailandPackage()
trip_to.detail()

from travel import veitnam
trip_to = veitnam.vietnamPackage()
trip_to.detail() #클래스 내의 디테일 함수

#__all__

from travel import*
trip_to = veitnam.vietnamPackage()
trip_to.detail()
#__init__ 에 __all__ = [] 하고 설정을 해주어야함
#클래스 내에서 if __name__ == "__main__" 을 해주면 외부에서 사용한건지 내부에서 사용한건지 알 수 있다.


#파일 경로 알기
import inspect #인스펙트.겟파일 하면 파일 경로를 알려줌
import random
print(inspect.getfile(random))

print(inspect.getfile(thailand))