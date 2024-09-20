import csv

csvFile = open( '202001_202408_주민등록인구및세대현황_월간.csv' , 'r' )   # 1.
csvContent = csv.reader( csvFile )              # 2.
newContent = list( csvContent )
인천광역시 = newContent[1]                       # 4. 인천 광역시 의 리스트
인천상반기인구수 = [ ]                            # 5. 인천 광역시 의 상반기 인구수 추출
남자인구수 =  [ ]
여자인구수 =  []
colNum = 1  # 총 인구수가 위치한 인덱스 번호
남자인덱스 = 4
여자인덱스 = 5
차이수 = []
개월수 = (12 * 4) + 8
###
날짜 = []
year = 20
month = 1
for date in range( 0 , 개월수 ) :
    month += 1
    if month > 12 :
        month = 1
        year += 1
    날짜.append( f'{year}/{month}')
###

for i in range( 0 , 개월수 ) :   # 상반기 총 6월 이므로 6회 반복
    print( 인천광역시[ colNum ] )
    인천상반기인구수.append( int( 인천광역시[colNum].replace( ",",'') ) )
    남자인구수.append(int(인천광역시[남자인덱스].replace(",", '')))
    여자인구수.append(int(인천광역시[여자인덱스].replace(",", '')))
    차이수.append( 여자인구수[-1] - 남자인구수[-1] )
    colNum += 6 # 총 인구수의 열번호가 6칸 마다 존재 # 열 이동
    남자인덱스 += 6
    여자인덱스 += 6
print( 인천상반기인구수 )



import matplotlib.pyplot as plt


plt.rcParams['font.family'] = "Malgun Gothic"      # 윈도우, 맑은고딕
plt.title('Line Chart')
plt.plot (  날짜 , 인천상반기인구수 , linewidth=5 )
plt.xlabel( '날짜')
plt.ylabel( '인구수(10,000,000) ' )
plt.xticks(rotation=50)
plt.show( )


plt.title('Line Chart')
plt.xlabel( '날짜')
plt.ylabel( '인구수(10,000,000) ' )
# plt.plot ( 날짜 , 남자인구수 , color = 'blue' , marker = 'o' , label='인천 상반기 남자인구수' )
# plt.plot ( 날짜 , 여자인구수 ,color = 'red' ,  marker = 'x'  , label='인천 상반기 여자인구수')
plt.plot ( 날짜 , 차이수 ,color = 'orange' ,  marker = 's'  , label='차이수')

plt.xticks(rotation=50)
# 범례 추가
plt.legend()
plt.show( )


colNum = 1  # 총 인구수가 위치한 인덱스 번호
서울 = newContent[2]                       # 4. 인천 광역시 의 리스트
서울인구수 = []
for i in range( 0 , 개월수 ) :   # 상반기 총 6월 이므로 6회 반복
    서울인구수.append( int( 서울[colNum].replace( ",",'') ) )
    colNum += 6 # 총 인구수의 열번호가 6칸 마다 존재 # 열 이동


colNum = 1  # 총 인구수가 위치한 인덱스 번호
부산 = newContent[10]                       # 4. 인천 광역시 의 리스트
부산인구수 = []
for i in range( 0 , 개월수 ) :   # 상반기 총 6월 이므로 6회 반복
    부산인구수.append( int( 부산[colNum].replace( ",",'') ) )
    colNum += 6 # 총 인구수의 열번호가 6칸 마다 존재 # 열 이동

fig, axes = plt.subplots( 2, figsize = (20,10))

axes[0].set_title('Line Chart')
axes[0].set_xlabel( '날짜')
axes[0].set_ylabel( '인구수(10,000,000) ' )
axes[0].plot ( 날짜 , 서울인구수 , color = 'blue' , marker = 'o' , label='서울인구수' )
axes[0].set_xticklabels( 날짜 , rotation=50)

axes[1].set_title('Line Chart')
axes[1].set_xlabel( '날짜')
axes[1].set_ylabel( '인구수(10,000,000) ' )
axes[1].plot ( 날짜 , 부산인구수 ,color = 'red' ,  marker = 'x'  , label='부산인구수')
axes[1].set_xticklabels(날짜 , rotation=50)

plt.subplots_adjust(hspace=0.4)  # You can change 0.4 to your desired spacing value
plt.show( )

