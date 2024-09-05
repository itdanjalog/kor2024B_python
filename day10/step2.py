# 실습1 : 계산기 , 기능/메소드/함수 : 1.더하기 2.빼기 3.곱하기 4.나누기
class Cal : # 클래스 선언 방법  # class 클래스명 :
    # 클래스명은 첫글자를 대문자
    def __init__( self , nickName ):
        self.nickName = nickName
    # 1.더하기 메소드(함수) # 함수 선언 방법 # def 메소드명( self , x , y ) :
    def add( self , x , y ):
        print( f'{x} + {y} = { x+y } ')
    # 2. 빼기 메소드( 함수 )
    def sub( self , x , y ) :
        print( f'{x} - {y} = { x-y }')
    # 3. 곱하기 메소드
    def mul( self , x , y ):
        return x * y # 반환/리턴/복귀 란 ? 함수를 호출했던 곳으로 자료/값 반환
    # 4. 나누기 메소드
    def div(self , x , y):
        z = x / y
        return z
# 같은 계산기 클래스를 이용한 2개의 계산기를 생성
c1 = Cal( '유재석계산기' ) # 계산기1 생성
c1.add( 3 , 5 )  # 3 + 5 = 8
c1.sub( 3 , 5 )  # 3 - 5 = -2
result1 = c1.mul( 2 , 3 )  # result1 = 6 ( c1.mul( 2 , 3 ) 의 실행 결과 )
print( result1 )
# a = input() # a변수에 input() 함수가 저장되는게 아니고 input()함수가 실행후 반환된 값을 저장
result2 = c1.div( 10 , 2 ) # result1 = 5.0 ( c1.div( 10 , 2 ) 의 실행 결과 )
print( result2)
c2 = Cal( '강호동계산기') # 계산기2 생성
c2.add( 7 , 3 ) # 7 + 3 = 10












