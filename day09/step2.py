'''
    객체
        주소 : 실제 컴퓨터에 저장된 객체가 위치한 메모리 주소 ( 16진수 )
            - 친구집에 컴퓨터를 사용 하기 위해 놀러갈 예정
            - 준비물 : 친구의 집주소 ( OOO아파트 302호 )
                - OOO아파트 302호로 이동

            - 객체의 속성/함수 를 사용 하기 위해
            - 준비물 : 객체의 주소 ( 302번지) , 객체의 주소를 관리 하는 방법 , 변수에 객체 주소값 대입
                - 주소를가지는변수명.

        객체의 멤버(속성/함수) 참조(이동) 하는 방법
            - .(도트연산자,참조연산자) : .변수가 가지고 있는 주소로 이동해서 속성/함수 호출
            참조변수.속성명
            참조변수.함수명( )
'''

# 제품 클래스 정의
class Product :
    # 클래스 속성 초기화 : 주로 객체들 마다 서로 같은 데이터를 저장할때 사용
    store = 'CU'
    # 객체 속성  초기화 : 주로 객체들 마다 서로 다른 데이터를 저장할때 사용
    def __init__(self , code , name , price , date ):
        self.code = code
        self.name = name
        self.price = price
        self.date = date
    # 함수 , self : 해당 함수를 호출 하는 객체 뜻 한다.
    def info( self ):                   # 매개변수x , 리턴값 x
        print( f'{self.store} {self.code} { self.name} {self.price} {self.date}')
    # 함수
    def priceUp( self , increase ):     # 매개변수o , 리턴값x
        self.price += increase
        # 해당 함수를 호출한 객체의price속성에 매개변수[increase] 값 만큼 더한다.
    # 함수
    def priceDown( self , reduction ):  # 매개변수o , 리턴값o
        self.price -= reduction
        # 해당 함수를 호출한 객체의price속성에 매개변수[reduction] 값 만큼 뺀다.
        return self.price   # 함수 종료시 함수를 호출했던곳으로 반환해주는 값
    # 함수
    def getPrice(self):                 # 매개변수x , 리턴값o
        return self.price

# 클래스를 이용한 객체 생성
    # Product(  1 , '사과' , 3000 , '2024-07-11' )    # 객체 생성 , 302번지 주소 생성
    # 변수명 = 302번지
p1 = Product(  1 , '사과' , 3000 , '2024-07-11' )
    # 변수에 302번지 대입 , 변수가 객체를 가지고 있다[x] 변수가 객체의 위치를 가지고 있다[o]
p2 = Product(  2 , '바나나' , 5000 , '2024-07-12' )    # 객체 생성 , 303번지 주소 생성
p3 = Product(  3 , '수박' , 7000 , '2024-07-13')

# [1] 객체를 가지는 변수를 호출
print( p1 ) # 0x000002185F47D790 , 객체가 위치한 컴퓨터 16진수 실제 메모리 주소
    # 변수 와 객체 는 서로 다른 구역
# [2] 해당 객체의 주소를 가지는 변수가 객체 에게 이동/참조
    # p1 : 참조변수 , 객체의 주소값(위치) 를 가지고 있는 변수
# 객체내 속성 호출
print( p1 )
print( p1.code )    # p1변수가 가지고 있던 객체위치에 code 속성 값 호출
print( p1.name )
print( p1.price )
print( p1.date )
print( f'{p2.code} {p2.name} {p2.price} {p2.date}' )
# 객체내 함수 호출
p1.info();p2.info();p3.info()
    # 주의할점
# info()    : 클래스 안에서 선언된 함수는 객체가 필요로 하다.
# 매개변수가 정의된 함수 호출
p1.priceUp( 10000 ) # 객체 생성시 3000 -> 13000
p1.info();p2.info();p3.info()

사과변동가격 = p1.priceDown( 5400 )    # 13000 - 5400 -> 7600
print( 사과변동가격 )

현재사과가격 = p1.getPrice()
print( 현재사과가격 )

# 클래스 속성의 값 호출
print( p1.store )   # 객체 생성시 store 속성의 값을 대입 하지 않고 클래스속성 초기화 된상태
print( p2.store )
print( p3.store )

# 클래스 속성 값 변경
p1.store = 'GS25'
p1.info();p2.info();p3.info()

# 객체의 속성 값 변경
p2.name = '델몬트바나나'
p1.info();p2.info();p3.info()
