# 3. 입력 ,
# 파이썬 문법/언어
# 주석 : 번역이 안되는 구역( 코드 설명 달기 )
# print( 리터럴 )  출력함수
# 제어/이스케이프 문자 : \t \n \' \" \\
print( "파이썬 2일차")
print( "\'파이썬\t2일차\n입니다.\'")

# 프로그램 : 명령어 집합 , 명령 : 컴퓨터에게 명령
# print() 출력 함수 : 컴퓨터에게 console 에 ~~~ 출력해
# input() 입력 함수 : 컴퓨터에게 console 에서 ~~~ 입력받아
input() # console창에서 입력받을 준비 되고 console창에서 사용자가 입력후 엔터
input('>> 입력 하기 전에 출력 되는 말 : ')

# 입력(input) 받은 내용물 출력(print) 해보자.
print( input('정수 입력해:') ) # input 실행하고 다음에 print
# ( 2 + ( 3 + 5) )   계산순서 : 3 + 5 먼저 계산하고 2 +

# 입력 받은 데이터의 타입/자료형 = 리터럴 : 정수 , 실수 , 논리 , 문자열
# 1.타입 확인 함수 : type( 데이터 ) : 데이터의 종류/타입 알려준다.
print( type(123) )      # 정수 == int
print( type( 3.14 ) )   # 실수 == float   #부동소수점
print( type(True) )     # 논리 == bool
print( type("파이썬") )  # 문자열 == str

# 2. 입력받은 데이터의 타입 확인하자
print( type( input( ) ) )
    # 실행순서 : input -> type -> print
    # 입력받고 타입확인하고 출력해
    # input() 함수는 문자열(str) 만 입력을 받는다. 그러므로 변환

# 3. 타입 변환  str -> int,float,bool 변경
    # int(데이터) : 데이터를 정수 형으로 변환 함수
    # float( 데이터 ) : 데이터를 실수 형으로 변환 함수
    # bool( 데이터 ) : 데이터를 논리 형으로 변환 함수
    # str( 데이터 ) : 데이터를 문자열 형으로 변환 함수
print( type( int( "123" ) ) )  # "123" 이라는 문자열은 123으로 정수(int)가 될수 있다.
# print( type( int( "a" ) ) ) #오류발생 : 왜? "a"는 정수(int)가 될수가 없다.
print( type( float( "3.14" ) ) )
print( type( bool( "True" ) ) )
print( type( "123" * 1 ) )
#print(  "123" + 1  )
print(  "123" + "456"  )

# 4.실습
    # 1. 문자열 을 입력받아 출력하시오.
print( input('문자열 : ') ) # input() 함수는 기본적으로 문자열을 입력받는다.
    # 2. 정수형 을 입력받아 출력하시오.
print( int( input("정수형 : ") ) )
    # 3. 실수형 을 입력받아 출력하시오.
print( float( input("실수형 : ") ) )
    # 4. 논리형 을 입력받아 출력하시오.
print( bool( input("논리형 : " ) ) )
