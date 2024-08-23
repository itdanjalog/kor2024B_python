# (3) range( ) : 숫자 리스트를 생성하여 반환 해주는 함수
    # range( 숫자 ) : 0부터 숫자 미만 까지 포함하는 range 객체를 만들어준다.
    # range( 시작숫자 , 끝숫자 ) : 시작숫자 부터 끝 숫자 미만 까지 포함하는 range 객체를 만들어준다.
    # range( 시작숫자 , 끝숫자 , 증감단위 ) : 시작숫자 부터 끝 숫자 미만 까지 증감단위 만큼 증감하여 포함하는 range 객체를 만들어준다.
a = range( 10 )
print( a ) # 0,1,2,3,4,5,6,7,8,9
a = range( 1 , 11 )
print( a ) # 1,2,3,4,5,6,7,8,9,10

# 예제
for value in range( 10 ) :      # 0 ~ 9
    print( value , end=' ' ) # print(    , end =' ' ) : 줄바꿈 처리를 하지 않는 출력문
print( ) # 예제 구분
for value in range( 1 , 11 ) :  # 1 ~ 10
    print( value , end= ' ')
print( ) # 예제 구분
for value in range( 1 , 11 , 2 ) :  # 1 ~ 10 , 2씩증가 , 1 3 5 7 9
    print( value , end= ' ')
print( ) # 예제 구분
# 예제2 1 부터 10까지의 누적합계를 구하시오.
sum = 0
for i in range( 1, 11 ) :
    sum += i
print( sum )

# 예제3 1 부터 100까지의 누적합계를 구하시오.
sum = 0
for i in range( 1 , 101 ) : # 1 ~ 101미만
    # print( i )
    sum += i
print( sum )    # 5050

# 예제4 구구단
# 1. 단출력 : 2~9
for 단 in range( 2 , 10 ) :
    print( 단 )
# 2. 곱출력 : 1~9
for 곱 in range( 1 , 10 ) :
    print( 곱 )
# 3. for문의 중첩 : 단 마다 곱 인지? [O] 곱 마다 단 인지? [X]
for 단 in range( 2 , 10 ) :
    # 들여쓰기 주의
    for 곱 in range( 1 , 10 ) :
        # 들여쓰기 주의
        print( f'{단} X {곱} = { 단*곱:>2}' , end = '     ')
    print()
