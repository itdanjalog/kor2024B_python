# 클래스와 객체 개념

# 함수 유형

# 간단한 실습
#[2] 클래스내 메소드(함수) 만들기
class FourCal : #(1) 클래스내 메소드 선언
    # 생성자 , 다중생성자 없다 ,
    def __init__(self , first , second ):
        self.first = first
        self.second = second
    # 함수 코드는 객체들이 공유  사용.
    def setdata(self , first , second ): # 함수/메소드 정의 # 매개변수란? 함수 호출시 전달되는 인자 값을 저장하는 변수
        self.first = first      # self(자신 객체) # self.first : 객체변수가 생성된다 # = 4
        self.second = second    # 함수를 호출한 객체(self)내 second 변수를 선언하고 매개변수(2)를 저장한다.
    def add(self):
        result = self.first + self.second   # self : 해당 함수를 호출한 객체 자신 # self.변수 ( 멤버 변수/필드 )
        return result
    def mul(self):
        result = self.first * self.second   # result 변수는 지역변수( 함수내에서만 사용되고 함수 종료시 사라진다. )
        return result                       # return 함수 종료시 함수를 호출 했던 곳으로 반환 되는 값
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

# a = FourCal() #(2) 객체 생성
# a.setdata( 4 , 2 )      #(3) 객체내 메소드 실행
# print( a.first )        #(4) 객체내 필드 값 호출
# print( a.second )
# print( a.add() ); print( a.mul() ); print( a.sub() ); print( a.div() );
#
# b = FourCal() #(3) 객체 생성 , a에 저장된 객체와 b에 저장된 객체는 다르다. 타입같지만.
# b.setdata( 3 , 7 )
# print( b.first )
# print( b.second )
# print( b.add() ); print( b.mul() ); print( b.sub() ); print( b.div() );

c = FourCal( 4 , 2 )#(4) 객체 생성 , 생성자 매개변수
print( c.first )
print( c.second )