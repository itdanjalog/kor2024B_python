# [실습4] 최근 한달 간의 전국 아파트 실거래가 분석
    # '인천시 부평구' 아파트의 실거래가 추출
    #  실거래가 공개시스템 - 국토교통부(https://rt.molit.go.kr/)
    #   1. 상단 메뉴 -> 자료 제공
    #   2. 아파트 -> 매매 -> 계약일자 : 2024-06-18 ~ 2024-07-18
    #   3. csv 다운 , 아파트실거래가.csv

import csv # csv 관련된 함수들을 제공

# 1. 파일 객체 호출
csvFile = open( '아파트실거래가.csv' , 'r' )
# 2. CSV 형식 으로 파일 읽어오기
csvContent = csv.reader( csvFile )
# 3. 리스트 타입 변환
newContent = list( csvContent )
# 4. # 16 인덱스 부터 마지막 인덱스 까지 만 사용.
newContent = newContent[ 16 : ]
# 5.
#aptName = input(' 부평구 아파트 :')
for row in newContent :
    시군구 = row[1]        # 시군구 추출
    #print( 시군구 )
    부평구색인 = 시군구.find( '부평구' )   # 문자열.find( 찾는문자 ) : 문자열내 찾는문자가 존재하면 인덱스반환 없으면 -1
    #print( 부평구색인 )
    if 부평구색인 >= 0  :
        #if row[5].find(aptName) >= 0 :
        print( f'단지명:{row[5]} {row[9]}만원' )