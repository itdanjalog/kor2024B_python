# [1] 파이썬에서 시각화 할수 있는 객체 모듈 가져오기
    # import : 현재 파일 외부에 있는 함수 또는 객체 가져오기 위한 키워드
    # as : 객체 또는 함수의 별칭 * 함수 또는 객체 이름이 길거나 복잡 할때 사용

import matplotlib.pyplot as plt
# - 다양한 시각화(차트) 옵션을 추가
plt.title('chart1') # [3] 차트 제목
YData = [ 5 , 2 , 7 , 1 ] # [4] Y축 데이터
plt.plot(  YData ) # [5] 선 차트 에 y축 데이터 대입
# [2] 시각화(차트) 실행
plt.show( )
# (2)
plt.title( 'chart2' )
XData = [ 10 , 20 , 30 , 40 ]   # X축 데이터
YData = [ 50 , 2 , 9 , 16 ]     # Y축 데이터
plt.plot( XData , YData )       # X축과 Y축 데이터를 선차트에 대입
plt.show( )
# (3) 제품별 판매량 시각화
plt.title( 'chart3' )
XData = [ 'cola' , 'cider' , 'fanta'  ]
YData = [  102 , 130 , 124 ]
plt.plot( XData , YData  , label = 'sales' ) # label='항목이름'
plt.xlabel('product')
plt.ylabel( 'sales' )
plt.grid()      # 눈금선 표시
plt.legend( )   # 범례 표시
plt.show( )
