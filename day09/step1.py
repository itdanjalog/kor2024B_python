'''
    # 객체이란 ? 고유성질 과 행위 가 존재하는 논리적/물리적 형태
        객체(Object) : 본인 외   , 나를 제외한 모든것
            - 공기o , 안경o , 사람o , 컴퓨터o, 의자o 등등
            - 수업o , 주문o , 축구o , 공부o , 판매o 등등
        vs
        주체(Subject) : 본인     , 개발자/나 (Subject)

        - 고유성질 : 속성을 뜻하고 데이터/값 를 의미하는 것
            자동차 예 -> 차량색상 : 검정색 , 속도 : 17km , 차량번호 : 1234 등등
            강의 예 -> 강사명 : 김현수 , 과목 : 파이썬
        - 행위 : 함수/메소드 을 뜻하고 여러개실행문을 의미하는 것
            자동차 예 -> 전진() , 후진() , 주차() , 와이퍼()
            강의 예 -> 쉬는시간() , 타자입력()

    # 클래스이란 ? 고유 성질 과 행위 를 미리 정의 하는것
        - 클래스 정의/만드는 방법
        class 클래스명( ) :
            def __init__( self , 속성명1 , 속성명2 ) :
                self.속성명1 = 속성명1
                self.속성명2 = 속성명2

            def 메소드명( self , 매개변수1 , 매개변수2 ) :
                실행문

        - 객체 정의/만드는 방법
        클래스명( 속성자료1 , 속성자료2 )

    객체란? 논리적/물리적 정의한 실체물
    클래스란? 객체를 물리적으로 표현하기 위한 설계도
    인스턴스란? 클래스를 이용해서 객체를 물리적[메모리]으로 만든 실체물
'''

'''
    이름 , 나이 , 도시락내용물 을 가지는 학생을 설계하시오.
        '유재석' , 40 , '컵라면' , '강호동' , 45 , '김밥'
    각 객체를 생성해서 도시락먹기 행위/함수를 실행했을때 각 객체가 가지는 도시락내용물을 출력하시오.
'''

# https://github.com/itdanjalog/tj_2024A_python/tree/master/src/day06

#(1) 간단한 클래스 , class 클래스명 :
class FourCal :
    pass # 아무것도 수행하지 않는 문법으로, 임시로 코드를 작성할때 주로 사용됨.
#(2) 객체 생성 , 클래스명()
a = FourCal()
print( type( a ) )  # <class '__main__.FourCal'> # type() 타입 반환해주는 함수

# 예)
# [1] 특정 프로그램의 방문록 들을 관리하는 메모리 설계
    # (게시물이 가질수 있는 속성/특성 ) 방문록번호,방문록내용,방문록작성일,방문록작성자 여러개 관리하는 클래스 설계
class Board :
    def __init__( self , 번호 , 내용 , 작성일 , 작성자 ):
        self.num = 번호
        self.content = 내용
        self.date = 작성일
        self.writer = 작성자
# 객체 생성
print(  Board( 1 , '안녕하세요' , '2024-07-11' , '유재석')  )
b1 = Board( 2 , '안녕하세요2' , '2024-07-12' , '강호동' )
print( b1 )

# [2] 특정 프로그램의 회원 들을 관리하는 메모리 설계
    # 회원번호 , 아이디 , 비밀번호  , 회원명 들을 가지는 속성을 여러개 관리하는 클래스 설계
class Member :
    def __init__(self , num , id , password , name ):
        self.num = num
        self.id = id
        self.password = password
        self.name = name
# 객체 생성
m1 = Member( 1 , "qweqwe" , "1234" , "유재석" )
m2 = Member( 2 , "asdasd" , "4567" , "강호동" )    # <__main__.Member object at 0x000001F67E4D83E0> 객체가 저장된 메모리의 위치번호
print( m1 )
print( m2 )

# [3] 특정 프로그램의 제품 들을 관리하는 메모리 설계
    # 제품코드 , 제품명 , 가격 , 등록일 들을 가지는 속성을 여러개 관리하는 클래스 설계
class Product :
    def __init__(self , code , name , price , date ):
        self.code = code
        self.name = name
        self.price = price
        self.date = date
# 객체 생성
p1 = Product(  1, '사과' , 3000 , '2024-07-11' )
p2 = Product(  2 , '바나나' , 5000 , '2024-07-12' )
print( p1 )
print( p2 )

# [ 실습 ] 자동차 들을 관리하는 메모리 설계
    # 색상 , 속도 , 제조사 , 차량 번호 들을 가지는 속성을 여러개 관리하는 클래스 설계
    # 임의 의 값으로 객체 2개 생성
class Car : # 추상적으로 생각한 (속성,함수)를 가지는 객체의 클래스를 설계
    def __init__(self , color , speed , manufacturer , carNumber):
        self.color = color      # 색상
        self.speed = speed      # 속도
        self.manufacturer = manufacturer    #제조사
        self.carNumber = carNumber  #차량번호
# 객체 생성 ( 클래스가 준비물 )
내차 = Car( '노랑' , 0 , '현대' , '1234' ) # 차 1대 생성
친구차 = Car( '빨강' , 0 , '기아' , '4567' ) # 차 1대 생성
    # **클래스/설계도 는 같지만 서로 다른 객체( 서로 다른 메모리 )가 만들어 진다.!!!!!!!!
print( 내차 )      # 0x000001CFD1E2F1A0
print( 친구차 )    # 0x000001CFD1E2F1D0