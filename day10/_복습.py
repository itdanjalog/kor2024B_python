'''
    절차지향 프로그래밍 언어 : C언어
    객체지향 프로그래밍 언어 : 파이썬,JAVA,JS
    객체지향
        - 객체 : 클래스 기반으로 할당된 메모리 공간
        - 클래스 : 객체를 만들기 위한 설계도
            - 속성( 객체내 변수 )  : 객체가 가지는 고유 성질
            - 메소드( 객체내 함수 ) : 객체의 행동
'''
# 시나리오1 예] 온라인에 쇼핑에서 쇼핑구현하기 위해 사람을 회원으로 구축
    # 오프라인 쇼핑은 내가 직접 가게에 가서 제품 확인 구매
    # 온라인 쇼핑몰 손님[사람] 설계( 이름,주소 ) 제품[신발]설계( 제품명, 가격, 사진 )
class Member : # 클래스의 선언
    # 생성자 : 객체가 생성될때 초기(처음에 속성에 값을 대입)화 역할 하는 함수
    def __init__( self , name , address  ):
        # self : 해당 함수를 호출한 객체를 지칭
        self.name = name
        self.address = address
# 1. '유재석' 와서 회원가입 ( 객체 생성 )
m1 = Member('유재석','인천시 부평구')
# 2. '유재석' 와서 회원가입 ( 객체 생성 )
m2 = Member('강호동','인천시 서구')
    # 두 객체는 설계도/클래스 는 같지만 서로 다른 형태/객체 이다.
# 3. 접근/도트 연산자[ . 포인터 ] : 해당 참조하는 곳으로 이동해~~
# m1.  # m1변수가 참조하는 객체로 이동해~~
print( m1.name )        # 유재석
print( m2.address )     # 인천시 서구
value = 3               # value가 참조하는 '3' 리터럴이 위치한곳으로 이동해~







