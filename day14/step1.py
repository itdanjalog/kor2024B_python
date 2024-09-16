
# 2. 해당 맷플롯 라이브러리 가져오기
import matplotlib.pyplot as plt # as [별칭] , plt 이라는 이름으로 해당 라이브러리 사용.

# [1] 선차트 예제1
plt.title('chart1')          # 차트의 제목 설정 .title('차트제목')
data = [ 5 , 2 , 7 , 1 ]    # 차트에 표현할 데이터 리스트
plt.plot( data )            # .plot( 데이터리스트 ) , 선차트 표현
plt.show()                  # 차트 실행

# [2] 선차트 예제2
plt.title('chart2')
xData = [ 10 , 20 , 30 , 40 ]           # x축 데이터 리스트
yData = [ 50 , 2  ,  9 , 16 ]           # y축 데이터 리스트
plt.plot( xData , yData )               # .plot( x축데이터리스트 , y축데이터리스트 )
plt.show()                              # 차트 실행

# [3] 선차트 예제3
plt.title('chart3')
xData = [ 'A' , 'B' , 'C' , 'D' ]
yData = [ 50  , 30  , 40  , 10 ]
plt.xlabel('x-axios label')             # .xlabel("x축제목") , x축의 레이블( x축 제목 )
plt.ylabel('y-axios label')             # .ylabel("y축제목") , y축의 레이블( y축 제목 )
plt.plot( xData , yData )
plt.show()

# [4] 선차트 예제4
xData = [ 'A' , 'B' , 'C' , 'D' ]
yData = [ 50  ,  30 , 40  , 10  ]

plt.plot( xData , yData )
plt.grid( ) # .grid() : x축과 y축에 수평/수직 선을 추가 한다. 보기 쉽게 해준다.
plt.show( )

# 실습1  : 아래의 리스트 를 활용 하여 날짜별 제품의 판매량 데이터 를 선 차트로 표현 하시오.
xData = [ '08-06' , '08-05' , '08-04' , '08-03' ]
yData = [ 321  , 124 , 534 , 297 ]

plt.plot( xData , yData )           # 차트 종류 : 선차트 에 데이터 들을 대입
plt.title( 'products sales')        # 차트 제목
plt.xlabel( 'date')                 # 차트 x축 제목
plt.ylabel( 'sales rate')           # 차트 y축 제목
plt.grid()                          # 차트 x축과 y축 의 수평/수직 선
plt.show()                          # 차트 실행
