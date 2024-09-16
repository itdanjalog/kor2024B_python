# 1. 맷플롯 라이브러리 호출
import matplotlib.pyplot as plt

# 2. 임의의 데이터 리스트
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 0.5, 1, 0.5, 0, -0.5, -1, -0.5, 0, 0.5, 1]
# 3.
plt.plot( x , y , label='y data' , color ='red' , linewidth=2 , marker = 'o' )
# label='범례이름' , color ='(영문)색상명' , linewidth=선굵기 ,  marker = '마커모양'
plt.title( 'Line Chart')
plt.xlabel( 'x-axios')
plt.ylabel( 'y-axios' )
plt.grid()
plt.legend()                    # .legend() : 범례 , 범례이름 : .plot( x축,y축,lebel="범례이름" )
plt.show()
# 4. 막대차트  : 각 막대의 길이가 데이터의 값을 나타낸다.
plt.bar( x , y  )               # .bar( x축데이터 , y축데이터 ) : 막대차트
plt.title('Bar chart')
plt.xlabel( 'x-axios')
plt.ylabel( 'y-axios')
plt.show()
# 5. 산점도 : x축 와 y축의 값의 관계를 시각화 한다. 각각의 데이터 포인트는 두 변수의 값을 x축과 y축에 대응시켜 점으로 표현.
import random # 난수 라이브러리 호출
    # random.random() : 0 ~ 1 사이의 난수 생성
    # [ 값 for _ in range( 숫자 ) ] : 숫자 만큼 값을 리스트에 대입한다.
x = [ random.random() for _ in range( 50 ) ]    # 0~1 사이의 난수를 50개 생성해서 리스트에 대입
y = [ random.random() for _ in range( 50 ) ]    # 0~1 사이의 난수를 50개 생성해서 리스트에 대입
plt.scatter( x , y , color = 'green' , s = 50 , edgecolors= 'black' )            # .scatter( x축데이터 , y축데이터  ) : 산점도
plt.show()

# 실습2 : 아래와 같은 데이터 리스트 를 활용 해서 제품의 재고 수량을 막대 차트로 표현 하시오.
products = [ 'coke' , 'cider' , 'beer' ]
stocks = [ 80 , 40 , 62 ]

plt.bar( products , stocks , color = 'orange' )      # 막대차트
plt.title( 'products stock')
plt.xlabel( 'names')
plt.ylabel( 'stock')
plt.show( )
