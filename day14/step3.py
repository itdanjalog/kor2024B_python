'''
    실습3 : 최근 30일의 간의 '삼성전자' 주가를 선 차트로 표현하시오.
        - '삼성전자'의 주가 정보의 csv 파일 필요
            삼성전자주가.csv
            1. 한국거래소 정보데이터 시스템 : http://data.krx.co.kr/
            2. '삼성전자' 검색
            3. 일자별 시세 탭
            4. 최근 한달 검색
            5. csv 파일로 내려받기
        - csv 파일의 날짜별 '종가' 를 차트로 표현
'''
import csv  # 1. csv 라이브러리 호출
csvFile = open( 'data_5115_20240920.csv' , 'r' )# 2.  해당 csv 파일 오픈
csvContent = csv.reader( csvFile )# 3. 해당 csv 파일 읽어와서 변수에 저장
날짜리스트 = [ ] # 차트에 표현할 날짜 목록/리스트
가격리스트 = [ ] # 차트에 표현할 가격 목록/리스트
for row in list(csvContent)[ 1 : ] : # 4. 읽어온 csv 파일 확인하기 , 리스트로 타입변환 ,첫번째 행 제거(슬라이싱 이용한 제거)
    # list( ) : 리스트 타입으로 변환 해주는 함수
    # print( row )
    # print( f'날짜 : { row[0]}')   # 날짜 , 첫번째 열
    # print( f'종가 : { row[1]}')   # 종가(가격) , 두번째 열
    날짜리스트.insert(0 , row[0].split("/")[1] +'/'+ row[0].split("/")[2] )      # 날짜리스트에 날짜 대입 , 연도 제거 , 월/일 표현
    가격리스트.insert( 0, int( row[1] ) )      # 가격리스트에 가격 대입 , 정수 타입 변환

import matplotlib.pyplot as plt

# 리스트 의 데이터들을 뒤집기 : 리스트명.reverse()


plt.title('Line Chart')
plt.plot( 날짜리스트 , 가격리스트 )
plt.xlabel( 'date')
plt.ylabel( 'price' )
plt.show( )

