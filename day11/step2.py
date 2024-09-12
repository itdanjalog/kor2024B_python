# [1] 예외 다중 처리 # 다중 except # 0개 또는 1개 실행
array = [ 1,2,3]
try :
    array[2]
    print( 4/0 )
    int( 'a' )
except IndexError as e :
    print( e )
except ZeroDivisionError as e :
    print( e )
except ValueError as e :
    print( e )

# [2] 모든 예외를 처리 하는 클래스 # 예외클래스 중에 상위 클래스 Exception 클래스
try :
    array[5]
    print( 4/0 )
    int( 'a' )
except Exception as e :
    print( e )
except ValueError as e:  # 아무런 의미가 없는 예외 # 앞에서 모든 예외를 처리 하니까.
    print( e )

# [3] finally 키워드 # 예외 발생 여부와 상관없이 무조건 실행되는 코드
try :
    array[2]
except IndexError as e :
    print( e )
finally :
    print('예외 여부와 상관없이 실행된다.')

# [4] pass 키워드 # 예외 회피 #예외 발생시 그냥 통과 # 아무것도 하지 않을때 사용
try :
    print( 4/0 )
except :
    pass # 만약에 예외가 발생하면 pass~

# [5] raise 키워드 # 예외 강제 발생 # 강제로 예외를 발생 시킬때 사용
try :
    raise ValueError    # 강제로 예외 발생
except ValueError as e :
    print( e )

# 실습1 :
    # 1. 이름(문자열) 2.나이(정수)를 입력받아 하나의 (member)딕셔너리 저장 하기 # 입력받을때 1가지 이상의 예외를 예측해서 예외처리 하기
    # 2. member 딕셔너리 내 'phone'이라는 key 의 value 를 호출 하기 # 호출시 예외발생 처리 하기
try :
    # 1.
    name = input( 'name : ' )
    age = int( input('age : ' ) ) # 나이 입력시 문자를 입력하면 예외발생 : ValueError
    # 2.
    dic = { 'name' : name , 'age' : age  }
    print( dic['phone'] )   # 딕셔너리내에서 존재하지 않는 key 사용 했을때 예외 발생 : KeyError
except ValueError as e :
    print( '나이를 숫자형식으로 입력 해주세요.')
except KeyError as e :
    print( '존재하지 않는 key 입니다.' )
except Exception as e :
    print( '예외발생 [관리자에게문의] ')
finally :
    print( '프로그램이 안전하게 종료 됩니다.')























