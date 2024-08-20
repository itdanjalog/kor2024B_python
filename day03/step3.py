# day03 > step3.py
'''
1. 연산자
    - 대입연산자 제외한 연산자 1개당 연산 결과의 자료값 은 항상 1개 이다.
2. 연산자 종류
    1. 산술연산자 : +더하기 , -빼기 , *곱하기 , **제곱 , / 나누기 , //몫 , % 나머지
    2. 연결연산자 : +문자열연결   ,(쉼표)문자열연결
    3. 비교연산자 : >초과/크다 , <미만/작다 , >=이상/크거나같다 , <=이하/작거나같다 , ==같다 , !=같지않다
        - 주의할점 : => 같거나크다X , =< 같거나작다X , =대입 vs ==같다
    4. 논리연산자 :
        and 이면서 면서 이고 그리고 , 모두 True 이면 결과도 True , 하나라도 False 이면 결과도 False
        or 이거나 거나 또는 하나라도 , 하나라도 True 이면 결과도 True
        not 부정 반대 , True -> False , False -> True
    5. 대입연산자 , 복합대입연산자
        1.  =  오른쪽 값을 왼쪽에 대입
        2. += , -= , *= , **= . /= , //= , %=
            - 복합대입연산자
'''
# [1] 산술연산자 , 반환 리터럴 : 정수,실수 : 문자열 자료 1개
print( 10 + 3 )     # 13
print( 10 - 3 )     # 7
print( 10 * 3 )     # 30
print( 10 ** 3 )    # 제곱 , 1000
print( 10 / 3 )     # 3.33333333
print( 10 // 3 )    # 3
print( 10 % 3 )     # 1
# [2] 연결연산자 , 반환 리터럴 : 문자열 자료 1개
print( "hello" + " python") # hello python
print( "hello" , "python" ) # hello python
# print( "hello" + " python"+3 ) # 오류 발생
# [3] 비교연산자 , 반환 리터럴 : 불리언 자료 1개
print( 10 > 3 )     # 10이 3보다 크다 , True(진실/참)
print( 10 < 3 )     # 10이 3보다 작다 , False(거짓)
print( 10 >= 3 )    # 10이 3보다 이상이다, True
print( 10 <= 3 )    # 10이 3보다 이하이다, False
print( 10 == 3 )    # 10이 3과 같다, False
print( 10 != 3 )    # 10이 3과 다르다, True

# [4] 논리 연산자
print( 10 > 3 and 20 > 15 ) # True
    #   True   and True => True
print( 10 > 3 and 20 > 30 ) # False
    #   True  and False => False
print( 10 > 3 or 20 > 15  ) # True
    #   True or True => True
print( 10 > 3 or 20 > 30 )  # True
    #   True or False => True
print( not ( 10 > 3 ) ) # True -> False

# [5] 대입연산자
var1 = 10  #  10 리터럴값을 var1 변수에 대입.
#(1) var1 변수의 10를 더해서 저장
var1 + 10
var1 = var1 + 10    # 20
    # 1. var1 변수의 값호출 , var1 = 10 + 10
    # 2. 연산 , var1 = 20
    # 3. 대입 , var1 ( 20 )
    # 짧게 작성하는 방법
var1 += 10          # 30
#좌항 += 우항 : 우항에 값을 좌항 값과 더한 후 좌항에 대입
print( var1 )       # 30
var1 -= 10          #   vs        var1 = var1 - 10
print( var1 )       # 20
var1 *= 10          #   vs        var1 = var1 * 10
print( var1 )       # 200
var1 **= 1          #   vs        var1 = var1 ** 1
print( var1 )       # 200
var1 /= 2           #   vs        var1 = var1 / 2
print( var1 )       # 100
var1 //= 2          #   vs        var1 = var1 // 2
print( var1 )       # 50
var1 %= 3           #   vs        var1 = var1 % 2
print( var1 )       # 3

# [6] 삼항 연산자 , 1.조건 2.참 3.거짓
    # [True실행문] if [조건문] else [False실행문]
        # 만약에 조건이 True이면 [True실행문] 실행
        # 만약에 조건이 False이면  [False실행문] 실행
    # 삼항 연산자 중첩
        # [True실행문1] if [조건문1] else [True실행문2] if [조건문2] else [False실행문]
point = 82
# 만약에 포인트가 90 이상이면 합격 이고 아니면 불합격 출력
print( '합격' if point >= 90 else '불합격' )
# 만약에 포인트가 90점 이상이면 '최우수' 80점이상이면 '우수' 그외 '장려' 출력
    # 조건문1 : 포인트가 90점 이상 , True : '최우수'
    # 조건문2 : 포인트가 80점 이상 , True : '우수' , False : '장려'
print( '최우수' if point >= 90 else '우수' if point >= 80 else '장려' )

# 실습1 : 기본급 과 수당 금액을 각 정수로 입력 받아 실수령액 계산후 출력하시오.
# 실수령액 계산법 : 기본급 + 수당 - 세금(기본급10%)

# [풀이1]
    # 1. 각 변수에 정수값 입력받기
기본급 = int( input('기본급 : ') ) # 정수1 입력 받기
수당 = int( input('수당 : ') )  # 정수2 입력 받기
    # 2. 연산하기
실수령액 = 기본급 + 수당 - (기본급*0.1)
        # 주의할점 : 컴퓨터는 %를 문자로 인식 , 퍼센트 모른다.
        # 1 : 100%  , 10 : 1000% , 0.1 : 10% , 0.01 : 1% , 0.001 : 0.1%
    # 3. 결과 출력
print( f'실수령액 : { 실수령액 } ')
