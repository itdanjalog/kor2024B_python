# 반복문 실습1 : 구구단 출력
# (1) 구구단 에서 2단 만 출력
# 반복문 없이 ,
    # 반복되는 코드 :  print( f'2 x  = { 2*  }')
    # 반복 되지 않는 코드 :  1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9
print( f'2 x 1 = { 2*1 }')
print( f'2 x 2 = { 2*2 }')
print( f'2 x 3 = { 2*3 }')
print( f'2 x 3 = { 2*4 }')
print( f'2 x 4 = { 2*5 }')
print( f'2 x 5 = { 2*5 }')
print( f'2 x 6 = { 2*6 }')
print( f'2 x 7 = { 2*7 }')
print( f'2 x 8 = { 2*8 }')
print( f'2 x 9 = { 2*9 }')
    # 반복문 변경
# 곱수는 1부터 10미만(9까지) 1씩증가하면서 곱수 변수에 대입 반복
for 곱수 in range( 1 , 10  , 1 ) :
    print(f'2 x {곱수} = { 2 * 곱수 }')

# (2) 구구단 출력 , for중첩
# 2-1 단 수 출력 , 2단 ~ 9단
# 단수는 2부터 10미만(9까지) 1씩증가하면서 단수 변수에 대입 반복 # 총 8회 반복
for 단수 in range( 2 , 10 , 1 ) :
    print( 단수 )
# 2-2 곱 수 출력 , 1곱 ~ 9곱
# 곱수는 1부터 10미만 1씩증가하면서 곱수 변수 대입 반복          # 총 9회 반복
for 곱수 in range( 1, 10 , 1 ) :
    print( 곱수 )

# 2-3 합치기 , 단 마다 곱 계산 O , 곱 마다 단 계산 X
for 단수 in range( 2 , 10 , 1 ) :          # 2~9 : 총 8회 반복
    for 곱수 in range( 1 , 10 , 1 ) :     # 단 1회전 할때 곱 9회전
        # 1~9 : 총 9회 반복 , 중첩 반복문 * 상위 반복횟수 = > 총 72회 반복
        print( f'{단수} x {곱수} = {단수*곱수}')

# 반복문 실습2 : 키보드로부터 끝값을 입력받아 1부터 입력받은 끝값까지 누적합계를 구하시오.
    # 1. 조건추가 : 값이 홀수 일때만 누적합계 구한다.
    # continue 키워드 : 가장 가까운 반복문으로 이동하는 키워드 (증감식)
    # 2. 조건추가 : 만약에 총 누적합계가 1000이상 되면 누적합계 계산을 (강제)종료한다.
    # break 키워드 : 가장 가까운 반복문의 탈출/(강제)종료
x = int( input() ) # 1. 정수 입력받기
sum = 0 # 2. 누적합계의 값을 저장할 변수
for var in range( 1 , x+1 ) : # 3. 1부터 x까지 1씩증가
    # 조건1
    if var % 2 == 0 : # 만약에 현재 반복변수의 값를 나누기 2 했을때 나머지가 1 이면 ( 짝수 )
        continue    # continue : 반복문 안에서 사용되는 키워드(문법)
        # 가장 가까운 반복문 으로 (코드 흐름) 이동 # continue 만나게 되면 아래 코드는 실행 되지 않는다.
    sum += var  # 위에서 continue 만났으면 실행안되는 코드 # continue 만나는 조건 : var % 2 == 1

    # 조건2
    if sum >= 1000 : # 만약에 현재 누적합계가 1000 이상이면
        break   # break : 반복문 안에서 사용되는 키워드(문법)
        # 가장 가까운 반복문 을 탈출/강제종료 하는 코드 # break 만나게 되면 아래 코드는 실행 되지 않는다.
print( f'sum : { sum }') # 만약에 10입력시 55가 출력 된다.

# 반복문 실습3 : 키보드로부터 입력을 무한루프(무한반복) 받는데 만약에 입력값이 'x' 이면 무한 반복 종료 하시오.
    # 무한루프의 주의할점 : 종료되는 조건을 판단 , break 키워드와 주로 사용된다.
while True : # while 반복문  # while 조건식 : # while True : 무한 루프
    print('무한 출력중') # 무한출력
    str = input('무한입력 : ') # 무한입력
    if str == 'x' : # 만약에 입력받은 값이 x 이면
        break # (무한)반복문 강제 종료



























