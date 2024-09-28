# 크롤링 실습1 : 할리스 커피 매장 위치 정보를 크롤링 하기
# https://www.hollys.co.kr/store/korea/korStore2.do
# 1. 할리스 커피 홈페이지 -> 2. 상단메뉴[ 매장] -> 매장검색
# 2. 크롤링 할 주소URL 확인
    # 1페이지 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store=
    # 2페이지 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=2&sido=&gugun=&store=
    # 3페이지 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=3&sido=&gugun=&store=
    # 4페이지 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=4&sido=&gugun=&store=
    # ~ 50페이지 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=50&sido=&gugun=&store=
# URL 패턴/중복 확인 : https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={ 페이지번호 }&sido=&gugun=&store=
# 3. 50페이지 URL 요청하고 응답 받아 보내기
#[1] request객체를 이용한 지정한url 요청 응답받기
import urllib.request           # 1. request객체 모듈 호출
from bs4 import  BeautifulSoup  # 5. BeautifulSoup 모듈 호출
# 11. 전역 리스트 # 전체 매장 리스트
매장목록 = []
# 4. 50번 반복 # for 반복변수 in range( 시작번호 , 끝번호(미만) )  # 시작번호 ~ 끝번호
for page in range( 1 , 51 ) :
    # print( page )
    # 파이썬 들여쓰기를 이용한 구역 부분
    #2. url 요청후 응답받기  # .urlopen('URL')  # pageNo 에 반복변수를 대입 # f포메팅
    응답변수 = urllib.request.urlopen( f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={ page }&sido=&gugun=&store=')
    #print( 응답변수 ) # 응답 결과는 객체 형식으로 <http.client.HTTPResponse object at 0x00000191C0934DC0>
    #3. 응답된 객체내 HTML 내용물 읽어드리기 # .read( )
    HTML데이터 = 응답변수.read()
    #print( HTML데이터 )
    # 5. BeautifulSoup 모듈 호출
    # 6. BeautifulSoup 객체 생성 # BeautifulSoup( html데이터 ,  'html.parser' )
    웹문서 = BeautifulSoup( HTML데이터 , 'html.parser')
    # 7. 특정 마크업 추출 # 매장 정보가 있는 HTML 테이블 마크업
    tbody = 웹문서.select_one('tbody') # <tbody> : 테이블 본문
    # print( tbody )
    # 8. 특정 마크업 추출 # 매장 정보가 있는 테이블 본문내 여러 행 마크업
    trs = tbody.select('tr') # <tr> : 테이블 행
    # print( trs )

    # 9. 반복문을 이용한 하나씩 행 확인 하기
    for tr in trs :
        # print( tr )
        # print( tr.select('td') ) # <td> : 데이블 데이터
        tds = tr.select('td')
        지역명 = tds[0].string # print( tds[0] )# 10. 지역명
        매장명 = tds[1].string # print( tds[1]) # 11. 매장명
        영업현황 = tds[2].string
        주소 =  tds[3].string
        전화번호 = tds[5].string
        # 10. 위 정보들을 이용한 리스트 선언
        매장정보 = [ 지역명 , 매장명 , 영업현황  , 주소  , 전화번호 ]
        # print( 매장정보 )
        # 11. 전역 리스트에 매장 리스트 추가 # 2차원 리스트
        매장목록.append( 매장정보 )
# 모든 for문이 종료 되었을때
print( 매장목록 )
# 생각해보기 : 매장목록 리스트 정보를 CSV 파일로 저장하기.
import csv # 1. csv 모듈 호출
파일객체 = open( '할리스매장정보.csv' , 'w' , newline='' , encoding='utf-8') # 2. 쓰기모드 파일 객체 생성
csv쓰기모드 = csv.writer( 파일객체 )# 3. csv 쓰기 객체 생성
csv쓰기모드.writerows( 매장목록 ) # 4. 쓰기 함수 # 2차원 리스트 writerows( )
파일객체.close()
print('-------- 매장 정보 크롤링 완료 -----------')









