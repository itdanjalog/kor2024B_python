# [실습2] :
# 행정안전부 홈페이지 -> 상단 메뉴(정책자료) -> 통계 -> 주민등록인구통계
# https://jumin.mois.go.kr/index.jsp
# 2024 06 ~ 2024 06 조회후 csv 파일 다운로드
# 다운로드 된 csv 파일을 현재 실습 폴더로 이동 시켜 주세요.

import csv

# (1) 해당 파일을 open해서 파일객체로 가져오기
csvFile = open( '202406인구통계.csv' , 'r' )
# (2) 해당 파일을 csv 함수( reader ) 이용한 파일 읽어오기
csvContent = csv.reader( csvFile )
# (3) 반복문을 이용한 행/줄 단위로 출력
for row in csvContent :
    print( row )
    # (4) 반복문을 이용한 현재 행/줄 단위의 열 단위 출력
    for col in row :
        print( col )

# 2024 6월 기준의 세대당 인구 수의 전국 평균
csvFile = open( '202406인구통계.csv' , 'r' )
csvContent = csv.reader( csvFile )
# 1. 리스트 타입 으로 변환
newContent = list( csvContent )
print( type( newContent ) )
print( newContent )

# 2. 첫번째 행 제거   , 제목 제거
newContent = newContent[ 1 :  ]
print( newContent )

# 3. 4번열( 3 인덱스 )
sum = 0     # 총합계
count = 0   # 총개수
for row in newContent :
    세대당인구수 = float( row[3] )    # 문자타입을 실수타입 변환
    print( 세대당인구수 )
    sum += 세대당인구수   # 세대당인구수의 누적 합계
    count += 1          # 지역 개수를 1씩 증가
# 5.
print( f'전국 세대당 인구수 평균 : { (sum/count):.2f} ')


# [실습3] 2024 01 ~ 2024 06 (상반기) 까지 인천광역시의 총 인구 증감 평균 계산
    #  2024 01 ~ 2024 06 검색후 csv 파일 다운로드
    #  2024상반기인구통계.csv
    # 인천광역시의 행/줄 : 6줄/행 , 인덱스 5
    # 월마다의 총 인구수 : 1월[1] 2월[7] 3월[13] 4월[19] 5월[25] 6월[31]
csvFile = open( '2024상반기인구통계.csv' , 'r' )   # 1.
csvContent = csv.reader( csvFile )              # 2.
newContent = list( csvContent )
인천광역시 = newContent[5]                       # 4. 인천 광역시 의 리스트
인천상반기인구수 = [ ]                            # 5. 인천 광역시 의 상반기 인구수 추출
colNum = 1  # 총 인구수가 위치한 인덱스 번호
for i in range( 0 , 8 ) :   # 상반기 총 6월 이므로 6회 반복
    print( 인천광역시[ colNum ] )
    인천상반기인구수.append( 인천광역시[colNum] )
    colNum += 6 # 총 인구수의 열번호가 6칸 마다 존재 # 열 이동

# 6. 인천 광역시 의 상반기 인구수 증감 추이
    # 리스트내 인덱스와 값 을 한번에 반복 : for index , value in enumerate( 리스트 ) :
상반기증가추이 = [ ]
for index ,인구수  in enumerate( 인천상반기인구수 ) :
    if index+1 > 5 : break
    현재달 = int( 인천상반기인구수[index].replace(",",'') )   # ,(천단위 쉼표) 제거 = 쉼표 를 공백 으로 치환 = 천단위 쉼표는 문자 타입 이라서 예산이 불가능.
    다음달 = int( 인천상반기인구수[index+1].replace(",",''))
    증감수 = 다음달 - 현재달
    상반기증가추이.append( 증감수 )
#
print( 상반기증가추이 )















