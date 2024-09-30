'''
    함수 : 함[상자] 수[숫자]
        - 상자 안에 들어있는 숫자 , 상자 안에 들어있는 코드 , 미리 작성된 코드/실행문
        - 코드/실행문 를 저장할때는 함수 , 자료/데이터 를 저장할때는 변수
        - 용어
            1. 매개변수 , 인자값 , 인수
            2. 반환값 , 리턴값 , 결곽값

        x , y               매개변수 : x , y
        -------------
        |           |
        |   z=x+y   |       함수 정의 :  z = x + y
        |           |
        -------------
        z                   반환값 : z

    재귀 함수 :
        재귀 : 자기 자신을 호출/참조
        재귀함수 : 함수 안에서 현재 함수를 다시 호출
'''
# [1] 기본 함수 정의
def 더하기함수( x , y ) :
    z = x + y
    return z
# [2] 기본 함수 호출
    # 1.
result = 더하기함수( 10 , 5 )
print( result )     # 15
    # 2.
print( 더하기함수( 5 , 3 ) ) # 8
    # 3.
result2 = 더하기함수( 8 , 2 ) + 10
print( result2 )    # 20

# 재귀함수 예시1 : 최대 996까지 의 재귀가 가능 하다.
'''
# [3] 재귀 함수 정의1
def refunction( ) :
    global i
    i += 1
    print( '함수 호출 횟수 : ' , i )
    refunction( ) # 함수내 재귀함수 호출
# [4] 함수 호출
i = 0
refunction()
'''
# 재귀함수 예시2
# [5] 재귀 함수 정의2
def refunction2( ) :
    global count
    count -= 1
    print( '함수 호출 횟수 : ' , count )
    if count == 0 :
        return
    refunction2() # 함수내 재귀함수 호출
# [5] 함수 호출2
count = 3
refunction2( )

# 재귀함수 예시3 : 누적합계  vs 반복문 과 비교
def refunction3( value ) :
    if value <= 1 : return 1    # 만약에 value가 1보다 이하이면 1 반환 하고 함수 종료
    return value + refunction3( value - 1 )

value = 100
result3 = refunction3( value )    # 1 ~ 5 까지의 누적 합계
print( '1~5 까지의 누적합 : ' , result3 )















