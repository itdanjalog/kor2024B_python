# [1] 고의적으로 예외 발생1 # 인덱스 # IndexError클래스
array = [ 1 , 2 , 3 ]
# array[5] # IndexError: list index out of range # 중간에 프로그램 종료
try :
    array[5]
except :
    print('IndexError 예외 발생') # IndexError 예외 발생 # 프로그램 유지

# [2] 예외 발생2 # 나누기 # ZeroDivisionError클래스
# print(  3/0 ) # ZeroDivisionError: division by zero
try :
    print( 3/0 )
except ZeroDivisionError as e : # except 예외클래스명 as 변수명 : # 변수명에 예외 사유를 대입한다.
    print( e )  # division by zero

# [3] 예외 발생3  타입변환 # ValueError클래스
# int( 'a' ) # ValueError: invalid literal for int() with base 10: 'a'
try :
    int( 'a' )
except ValueError as e :
    print( e )













