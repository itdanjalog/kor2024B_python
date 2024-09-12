# https://github.com/itdanjalog/tj_2024A_python/blob/master/src/day07/3_%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC.py

'''
    1_exception.py
    예외처리
        오류[Error] :
            - 시스템이 종료 되어야 할 수준의 상황과 같이 수습할수 있는 심각한 문제
            - 개발자가 미리 예측하여 방지할수 없다. 주로 하드웨어(메모리) 관련된 오류가 발생한다.
        예외[Exception]
            - 개발자가 구현한 로직에서 발생한 실수 나 사용자의 영향에 의해 발생 하는 문제
            - 오류 와 달리 개발자가 미리 예측하여 방지할 수 있기에 상황에 맞게 예외처리를 해야한다.
            - 개발자 예측 --> 개발자가 경험 풍부 --> 개발자의 경험 의존성 크다.

        - 왜?? 문제 가 발생하면 프로그램 자동으로 종료된다. - 문제가 발생해서 프로그램이 꺼지면 사용자에게 프로그램 사용에 있어 불편하다.
        - 예외가 발생 했을때 프로그램이 종료되지 않고 다른 흐름 으로 제어 하는 방법. 예외 처리

        - 예외처리 방법
            try :
                예외가 발생 하거나 발생 할 것같은 코드
            except :
                만약에 try 에서 예외가 발생 했을때 실행 되는 코드
            else :
                만약에 try 에서 예외가 발생 안 했을때 실행 되는 코드
            finally :
                예외 발생 여부 와 상관 없이 무조건 실행 되는 코드
'''
# [1] 들여쓰기 또는 내어쓰기의 문법 작성 문제 발생
print( 'python code' )
    # print( 'python code2')  # IndentationError: unexpected indent

# [2] 타입이 일치 하지 않을때 문제 발생
# print( int( input('숫자입력 : ') ) )    # a입력했을때 : ValueError: invalid literal for int() with base 10: 'a'

# [3] 존재하지 않는 인덱스를 호출했기 때문에 문제 발생
list = [ ]
# print( list[3] )    # IndexError: list index out of range

# ======= 예외처리 ========= #
# [1]
try :
    print( input('정수입력 : ') >= 5 ) # TypeError 예외발생 --> except 이동
    print( '정상 실행') # 위에서 예외 발생시 실행이 안됨.
except :
    print( '예외 발생')
# [2]
try :
    num = int( input( '정수입력: ' ) )  # ValueError 예외발생 -->  except 이동
except : # try 에서 예외가 발생 했을때 실행 되는 코드
    print( '비정상적인 실행 : 정수만 입력해주세요.' )
# [3]
else : # try 에서 예외가 발생 안 했을때 실행 되는 코드
    print( '정상적인 실행')
# [4]
finally:
    print( '입력 종료' )

# 실습1 : 입력 예외 처리
'''
while True :
    try : # 예외발생 하거나 할것 같은 코드 ( 예측 )
        ch = int( input('1.create 2.read : ') )
        if ch == 1 :
            print( 'create code')
        if ch == 2 :
            print( 'read code' )
    except :
        print( '비정상적인 입력입니다.' )
    else:
        print( '정상적인 입력입니다.')
    finally :
        print( '다시 입력받습니다.' )
'''
# 실습2 : 두개의 실수를 입력 받아 나누기 하시오.
    # 단 : 입력 받을때 0 입력시 예외처리를 하시오.

# 1. 예외발생 예측 : input 입력받은 문자열을 float 변환하는데 실수로 변환할수 없는 데이터는 예외발생  ValueError
    # "10.5" --> float("10.5")  예외발생 안함
    # "a" --> float("a")        예외발생 함
# 2. 예외발생 예측 : 나누기 할때 0 의 데이터는 나누기를 할수 없어. 예외발생  ZeroDivisionError
try :
    f1 = float( input('[1] float input : ') )   # 실수값을 입력받아 변수에 저장
    f2 = float( input('[1] float input : ') )   # 실수값을 입력받아 변수에 저장
    result = f1 / f2  # 나누기
    print( result )
except :
    print( '[예외발생] 실수 형식 으로 입력 하세요.' )
    print( '[예외발생] 0 은 나누기 할수 없어요. ')
    # 다음 학습 : 서로 다른 예외가 발생 했을때 서로 다른 흐름 제어 방법






