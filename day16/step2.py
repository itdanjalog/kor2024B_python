# 크롤링 실습2 : 예스24(서점)의 베스트셀러 도서 크롤링 하기
# 카테고리 : 소설/시/희곡 , 에세이 , IT 모바일
# 각 카테고리의 베스트셀러 도서정보(순위,도서명,저자) 크롤링 하기

# 1. URL 파악
# 소설/시/희곡  : https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=24&categoryNumber=001001046
# 에세이       : https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=24&categoryNumber=001001047
# IT 모바일    : https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=24&categoryNumber=001001003
# 패턴 분석 : 001001046(소설/시/희곡 식별번호) , 001001047(에세이 식별번호) , 001001003(IT모바일 식별번호)

# 0. 각 모듈 호출
import urllib.request
from bs4 import BeautifulSoup

# 2. URL 요청 응답 받기
categoryList = [ '001001046' , '001001047' , '001001003' ]
# 3. 반복문을 이용한 여러개 카테고리 url 요청 # for 반복변수 in 리스트 :
for category in categoryList : # 리스트내 요소(카테고리번호)를 하나씩 추출 # f포메팅   f'문자열{ 변수 또는 리터럴 또는 연산}문자열'
    url = f'https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=24&categoryNumber={ category }'
    response = urllib.request.urlopen( url )
    htmlData = response.read()
    #print( htmlData )
    # 4. BeautifulSoup 객체 이용한 마크업 추출 , 도서정보(순위,도서명,저자)
    soup = BeautifulSoup( htmlData , 'html.parser')
    contents = soup.select_one('#yesBestList') # 식별자 작성법 : 1.마크업 - '마크업명'  2.class - '.class명'  3.id - '#id명'
    rows = contents.select( 'li' ) # 모든 행 추출 # 행마다( 도서정보 1개 마다)
    for row in rows : # 모든 행들을 하나씩 추출하자.
        #print( row ) # 도서정보 한줄씩 추출
    # 5. 도서정보 자료에서 도서명 추출하기 # 제목의 마크업 : <a class="gd_name" href="/Product/Goods/104663596" onclick="wiseLogV2('BS', '001_005_001', ''); ">언젠가 우리가 같은 별을 바라본다면</a>
        gdname = row.select_one('.gd_name')
        # print( gdname )
        if gdname != None : # 만약에 데이터가 없는 부분 제외 # None 아니면
            bookName = gdname.string
            # print( bookName )
    # 6. 도서정보 자료 에서 저자 추출하기  # 저자의 마크업
        authpub = row.select_one('.authPub') # <span class="authPub"> <a> 차인표 </a> </span>
        if authpub !=None :
            authpub_a = authpub.select_one('a')
            bookAuth = authpub_a.string
            # print( bookAuth )
            # 확인차
            print( f'도서명 : { bookName }   저자 : { bookAuth }')
