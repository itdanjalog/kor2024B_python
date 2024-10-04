# 함수 사용 : 1. 함수 정의(만들기) 2. 함수 호출(사용)
# 함수를 정의하는 경우는 파이썬 회사에서 제공하지 않는 함수를 사용할때.
# 함수를 정의하지 않는 경우는 파이썬 회사에서 제공하는 함수가 존재할때. = 라이브러리/모듈
    # print() , input() , int() ,open() 등등 * 파이썬은 풍부한 라이브러리를 제공한다.

#[1] 기본 함수 정의/만들기
def 더하기함수( x , y ) : # 함수 선언 # 매개변수 2개 x , y
    z = x + y # 함수 정의
    return z # 함수 반환
#[2] 함수 사용 하고 매개변수 값(인수) 전달하여 결과 1개를 반환받아 변수에 저장
result = 더하기함수( 10 , 5 )
print( result ) # 15

'''
# [3] 재귀 함수 예1] 최대 파이썬에서는 재귀호출을 996회로 제한하고 있다.
#   [Previous line repeated 996 more times]RecursionError: maximum recursion depth exceeded
def refunction( ) :
    global i
    i += 1 # i는 1 누적 증가
    print( f'함수 호출 횟수 : { i }')
    refunction() # 재귀함수 호출 # 현재 함수내에서 동일한 함수를 호출한다.
# [4] 함수 호출
i = 0
refunction()
'''
# [5] 재귀함수 예시2]
def refunction2( ) :
    global count # glopal 이란 ? 함수 밖에 있는 전역변수를 함수 안으로 호출 하는 방법 키워드
    count -= 1 # count에 1 누적 차감
    print( f'함수 호출 횟수 : { count }') # print 몇번 실행 될까요?
    if count == 0 : # 만약에 count가 0이면 함수 종료
        return
    refunction2() # count가 0이 아니면 재귀함수
# [6] 함수2 호출
count = 3
refunction2()
'''
    (1) refunction2( )  
    count = 3 ---->  -1  ---->  count = 2 ----> print() ----> if count == 0 ----> false (6)함수종료
    (2) refunction2( )  
    count = 2 ---->  -1 -----> count = 1  ----> print()  ----> if count == 0 -----> false (5)함수종료
    (3) refunction2( )  
    count = 1 ---->  -1 ---->  count = 0 -----> print()  ----> if count == 0 ------> true (4)함수종료
'''
# 재귀함수 실습1 : 1~5 까지의 누적 합계를 구하시오.
# (1) 반복문 방법1
sum = 0
for value in range( 1 , 6 ) :
    sum += value
print( sum ) # 15

# (2) 재귀함수 방법2 # 코드 보면서 학습 어렵다. 해당 코드를 순서도를 작성하면서 이해를 하자.
sum = 0
def refunction3( value ) :
    if value <= 1 :
        return 1
    return value + refunction3( value - 1 )
sum = refunction3( 5 ) # 15
print( sum )

# 재귀함수 실습2 : 5! 의 팩토리얼 구하시오. 팩토리얼 란? 지정한 수보다 작거나 같은 모든 양의 정수의곱
#  5! 의 팩토리얼 결과는 5 * 4 * 3 * 2 * 1  계산한 결과
#  3! 의 팩토리얼 결과는 3 * 2 * 1 계산한 결과
# (1) 반복문 방법1
result = 1
for value in range( 1 , 6 ) :
    result *= value # 누적 곱하기
print( result ) # 120
# (2) 재귀함수 방법2
def refunction4( value ) :
    if value == 0 :
        return 1
    return value * refunction4( value - 1 )# 재귀 호출
print( refunction4(5) ) # 120































