'''
    연산자 : 연산/계산 할때 사용 되는 문자/기호
        - 수학에서 사용되는 연산자 와 비슷 , 다른 프로그래밍 언어 들과도 비슷 , 조금의 차이는 있다.

    연산자 종류
        1. 문자 연결 연산자 : '문자열'+'문자열'
        2. 산술 연산자 : 값(정수,실수) 반환
            + 더하기 , - 빼기 , * 곱하기 , ** 제곱
            / 나누기 , // 나누기 후 몫 , % 나누기 후 나머지
        3. 비교 연산자 : True or False 반환
            >초과,크다
            <미만,작다
            >=이상,크거나같다
            <=이하,작거나같다
            == 같다
            != 다르다
        4. 논리연산자 : True or False 반환
            - 비교연산자 2개 이상일때 주로 사용됨.
            and : 그리고, 이고, 모두 등등 / 비교연산자가 모두 True 이면 결과도 True
                ex) 성별이 남자 이면서 나이가 19세 이상 입니다. => 성인 남자.
                gender == '남' and age >= 19     , 초콜릿 이면서 사탕 먹을래
            or  : 이거나, 거나, 또는 등등 / 비교연산자가 하나라도 True 이면 결과도 True
                ex) 성별이 남자 이거나 나이가 19세 이상 입니다. =>
                gender == '남' or age >= 19      , 초클릿 이거나 사탕 먹을래
            not : 부정, 반대
                True => False , False => True

        5. 대입, 대입복합연산자
            =   : 오른쪽 값을 왼쪽에 대입
            +=  : 오른쪽 값을 왼쪽값에 더한 후 결과를 왼쪽에 대입
                age = age + 10   vs   age += 10
            -= , *= , **= , /= , //= , %=
            오른쪽 값을 왼쪽값에 연산 후 결과를 왼쪽에 대입

        6. 삼항연산자
            [True실행문] if [조건문] else [False실행문]
                - 만약에 조건이 True 이면 True실행문이 실행
                - 만약에 조건이 False 이면 False실행문이 실행
            [True실행문1] if [조건문1] else [True실행문2] if [조건문2] else [False실행문]
                - 삼항연산자는 중첩이 가능하다.

'''
#1.문자( '' 혹은 "" 감싼 텍스트 ) 연결연산자
print( '파이썬 ' + " 자바" )     # '문자열'+"문자열"
# print( '점수 : ' + 70 )         # '문자열' + 정수
print( '점수 : ' , 70 )         # print( '문자열' , 값 )
점수 = 98 # 변수란? 1개의 자료/데이터를 저장할수 있는 공간
# '점수' 변수명의 상자/메모리 에 98 라는 데이터/메모리 저장
print( '점수 : ' , 점수 )       # print( '문자열' , 변수명 )

#2. 산술연산자
print( 10 + 3 ) # 13
print( 10 - 3 ) # 7
print( 10 * 3 ) # 30
print( 10 ** 3 ) # 1000
print( 10 / 3 ) # 3.333333~~
print( 10 // 3 ) # 3
print( 10 % 3 ) # 1

#3. 비교연산자
print( 10 > 3 )     # True 진실
print( 10 < 3 )     # False 거짓
print( 10 >= 3 )    # True 진실
print( 10 <= 3 )    # False 거짓
print( 10 == 3 )    # False 거짓
print( 10 != 3 )    # True 진실

#4. 논리연산자
print( 10 > 3 and 10 > 5 )
    #   true  and  true  => true
print( 10 > 3 and 10 > 20 )
    #   true  and  false => false
print( 10 > 3 or 10 > 5 )
    # true or true => true
print( 10 > 3 or 10 > 20 )
    # true or false => true
print( not (10 > 3) ) # not true -> false

#5. 대입연산자
age = 19
print( age )
# 복합대입연산자
age = age + 10
    # 위 코드문장에서 연산자는 2개
    # 누구를 먼저 처리할까??  # + 더하기 처리 후 대입
print( age ) # 29
age += 10
print( age ) # 39
age -= 10
print( age ) # 29
age *= 10
print( age ) # 290
age **=1
print( age ) # 290
age /= 2
print( age ) # 145.0
age //= 2
print( age ) # 72.0
age %= 2
print( age ) # 0

# 삼항연산자
mathPoint = 82
# 만약에 수학점수가 90점 이상이면 '합격' 아니면 '불합격' 출력 하자
print( '합격' if mathPoint >= 90 else '불합격' )
# 만약에 수학점수가 90점 이상이면 '최우수' 80점 이상이면 '우수' 그외 '장려' 출력 하자
print( '최우수' if mathPoint >=90 else '우수' if mathPoint >=80 else '장려' )



