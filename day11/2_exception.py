'''
    2_exception.py
        예외 클래스 와 다중 except
            - except 키워드 에서 특정 예외를 처리할수 있다.
            - 예외 클래스를 이용한 특정 예외 처리하기
        사용방법
            try :
                예외가 발생 하거나 할 것 같은 코드
            except 예외클래스명 as 객체변수명 :
                예외가 발생 했을때 실행코드 , 객체변수에 예외가 발생한 이유가 저장된다.

        예외 클래스 종류
            - 예외 발생 정보를 가지고 있는 클래스
            0. Exception    : 모든 예외 클래스의 최상위 클래스 로써 , 모든 예외의 정보를 담을수 있다.
                - 다중 except 에서 사용시 마지막 에 사용한다.
            1. ValueError   : 숫자로 변환할수 없을때, 매개변수의 값이 적절하지 않을때 예외 발생.
            2. IndexError   : 리스트내 존재하지 않는 인덱스를 호출했을때 예외 발생
            3. ZeroDivisionError :  0 으로 나누기 할때 예외 발생
            4. TypeError : 잘못된 데이터 타입의 값이 사용될 때 예외 발생
            5. KeyError : 딕셔너리 에 존재 하지 않는 키를 호출 할때 예외 발생
'''
try :
    # int( input( '정수 입력:' ) )   # invalid literal for int() with base 10: 'a'
    # valueList = [ ]
    # print( valueList[3] )         # IndexError: list index out of range
    # print( 13 / 0 )               # division by zero
    # print( "python" + 5 )         # TypeError: can only concatenate str (not "int") to str
    valueDict = { 'name' : 'kim' }
    valueDict['age']                # KeyError: 'age'

except ValueError as e1 :
    print( e1 ) # invalid literal for int() with base 10: 'a'
    print( '정수 형식으로 입력해주세요. ' )
except IndexError as e2 :
    print( e2 )
    print( '존재 하지 않는 인덱스를 호출했어요.')
except ZeroDivisionError as e3 :
    print( e3 )
    print( '0으로 나누기 할수 없어요.')
except TypeError as e4 :
    print(e4)
    print( '잘못된 데이터 타입의 값 입니다.')
except KeyError as e5 :
    print( e5 )
    print( ' 딕셔너리 내 존재 하지 않는 키 입니다.')
except Exception as e0:
    print(e0)
    print('예외발생 ')
else :
    print( '정상실행')
finally :
    print( '처리종료' )

# 실습1 :
    # 1.이름(문자열) 과 나이 (정수)를 입력받기 , 입력 받을때 예외 발생을 예측 하여 예외 처리 코드 작성
    # 2. member 딕셔너리 내 'phone' 키의 값을 호출시 , 예외처리 코드 작성
    # 3. memberList 리스트 내 100번 인덱스의 값을 호출시 , 예외철 코드 작성
try:
    name = input( 'name : ')
    age = int( input('age : ') )
except ValueError as e :
    print( e )

try :
    member = { name : name , age : age }
    member["phone"]
except KeyError as e :
    print( e )
except NameError as e : #  존재 하지 않는 변수명 를 호출했을때 예외발생 클래스
    print( e )

try :
    memberList = [ ]
    memberList[100]
except IndexError as e :
    print( e )




















