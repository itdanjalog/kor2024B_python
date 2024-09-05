'''
    변수 : 하나의 자료를 저장 하는 메모리
        - 선언/정의/만들어지는 위치에 따라 구분한 변수
        - 전역변수, 지역변수 , 매개변수 , 객체변수, 클래스변수
    함수 : 여러개 의 실행문 을 저장 하는 메모리
        - 함수 : 클래스밖에서 정의된 함수
        - 메소드 : 클래스안에서 정의된 함수
    - 메소드
        - 클래스 안에서 선언되는 함수
        - 객체의 행동
'''
# 예] 학생 설계 , (변수/자료) 이름 , 도시락  (행동/실행) 밥먹기
class Student :
    # 생성자
    def __init__(self , name ):
        self.name = name
        # 객체 생성시 값을 대입 하지 않을 때는 정의만 하고 None 대입 권장
        self.도시락 = None
    # 메소드
    def 도시락주기( self , 도시락 ):
        print( f'{ self.name } 에게 { 도시락 } 도시락 대입/저장 ' ) #
        self.도시락 = 도시락
    # 메소드
    def 도시락먹기(self):
        print( f'{ self.name}이 { self.도시락 }를 먹습니다.' )

# 1. 유재석 학생(객체) 탄생 , name 은 태어나면서 할당 ( 생성자 )
s1 = Student( '유재석' )
# 2. 강호동 학생(객체) 탄생
s2 = Student( '강호동' )
# 3. 함수를 이용한 객체변수에 대입(행위)
s1.도시락주기('삼각김밥') # 유재석 에게 삼각김밥 주는 행위
s2.도시락주기('컵라면')
# 4.
s1.도시락먹기()  # 유재석이 삼각김밥를 먹습니다.

















