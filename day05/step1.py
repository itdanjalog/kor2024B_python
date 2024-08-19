
# 아래코드는 동일한코드가 5번 중복이 된다.
    # 동일한코드를 반복처리??? --> for문 문법
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
    # 위코드를 반복문으로 대체
for count in range( 5 ) :
    print('파이썬 ' , count )
for count in range(3) :
    print( count )
# 총 반복횟수 : range( ) 안에 작성한 수 만큼  => 3
# count 반복 변수에 저장된 값은 :  0 그리고 1 그리고 2  , 하나씩 순서대로 하나씩 저장
print( 0 )
print( 1 )
print( 2 )

# [예제1]
for x in range( 3 ) :
    print( x , '번 실행중') # x : 1 , 2 , 3
# [예제2]
for x in range( 1 , 5 ) :
    print( x , '번 실행중') # x : 1 , 2 , 3 , 4
# [예제3]
for x in range( 3 , 10 , 2 ) :
    print( x , '번 실행중' ) # x : 3 , 5 , 7 , 9

# [실습1] 1부터 100까지 출력 하시오.
for value in range( 1 , 101 ) :
    print( value )

# [실습2] 1부터 100까지 11의 배수만 출력 하시오.
for value in range( 1 , 101 ) :
    if value % 11 == 0 :
        print( value )

# [실습3] 1부터 100까지의 값을 총 더하기 한 누적합계를 출력하세요.
sum = 0 # 누적합계를 저장할 변수
for value in range( 1 , 101 ) :
    sum = sum + value # vs sum += value
print( '총 누적합계 : ' , sum )

# [실습4] 1부터 100까지 3배수만 출력하시오.
for value in range( 0 , 101 , 3 ) :
    print( value )

# [실습5] 1부터 100까지 홀수만 출력하시오.
for value in range( 1 , 101  ) :
    if value % 2 == 1 :
        print(value)

# [문제1] 구구단 출력 하시오. 2단 만 출력하세요.
print(' 2 X 1 = 2') # range( 1 , 10 , 1 )
print(' 2 X 2 = 4')
print(' 2 X 3 = 6')
print(' 2 X 4 = 8')
print(' 2 X 5 = 10')
print(' 2 X 6 = 12')
print(' 2 X 7 = 14')
print(' 2 X 8 = 16')
print(' 2 X 9 = 18')

for 곱 in range( 1 , 10 , 1 ) :
    print(' 2 X ',곱,'=',2*곱)

# [문제2] 구구단 출력 하시오. 2단~9단 출력하세요.
# 단 : 2 ~ 9
for 단 in range( 2  , 10 , 1 ) :
    print( 단 )
# 곱 : 1 ~ 9
for 곱 in range( 1 , 10 , 1 ) :
    print( 곱 )

# for문 중첩 : 단 마다 곱 [O] , 곱마다 단[X]
    # '단' 안에 '곱' 존재
for 단 in range( 2  , 10 , 1 ) :     #for 반복수 : 8
    for 곱 in range( 1, 10, 1):      #for2 반복수 : 72( 위for문 1회전할때마다 9회전 ) 9*8
        print( 단 , 'X' , 곱 , '=' , 단*곱 ) # 72번 출력


