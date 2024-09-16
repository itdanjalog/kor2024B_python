# 3_crawling.py

# 실습1 : 웹 페이지 의 HTML 호출
    # 인터넷에서 'http://quotes.toscrape.com' 접속
from bs4 import BeautifulSoup   # 크롤링 할때 사용되는 함수를 제공하는 라이브러리
import urllib.request           # url(인터넷주소) 요청 함수를 제공하는 라이브러리

# 1-1 분석할 인터넷주소(url)를 변수에 저장한다.
url = 'http://quotes.toscrape.com'
# 1-2 인터넷주소의 HTML를 요청한다.
    # urllib.request.urlopen( "url주소" ) : 해당 url주소의 HTML 요청한다.
HTMLreq = urllib.request.urlopen( url )
# 1-3 요청된 html를 읽어드린다.
HTMLData = BeautifulSoup( HTMLreq.read() , "html.parser" )
# 1-4 확인
# print( HTMLData )
# 웹페이지의 특정한 정보만 추출 --> 분석 ( 크롬 브라우저에서 F12 입력시 '개발자도구' 에서 html 확인 )
# 1-5 명언(quote)  , <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork"> </div>  추출
HTMLdivs = HTMLData.find_all( 'div' , class_="quote" )
# print( HTMLdivs )
for div in HTMLdivs :
    # <span class="text" itemprop="text"> ~~~ 명언 ~~~~ </span> 추출
    span = div.find( 'span' , class_="text")
    # ~~~ 명언 ~~~~ 추출
    print( span.text )


# 실습2 : 웹 페이지의 인터넷 기사 본문을 크롤링 하기 + 파일 처리
# 실습준비물 : 임의의 인터넷 기사 주소 'https://v.daum.net/v/20240801162402760'

# 2-1 분석할 인터넷주소(url)를 변수에 저잔한다.
url = 'https://v.daum.net/v/20240801162402760'
# 2-2 인터넷주소의 HTML를 요청한다.
HTMLreq = urllib.request.urlopen( url )
# 2-3 요청된 HTML를 읽어드린다.
HTMLData = BeautifulSoup( HTMLreq.read() , "html.parser")
# print(HTMLData) #확인
# 2-4 본문 추출
HTMLPs = HTMLData.find_all( 'p' )
# print( HTMLPs )#확인

# 크롤링 를 이용한 뉴스 본문을 메모장txt 파일에 저장하기 ( 파일처리 )
file = open( '뉴스크롤링.txt' , 'w' , encoding='utf-8' )

# 2-5 반복문 처리
for p in HTMLPs[ 2 : len(HTMLPs)-3 ] :    # 앞에 있는 <p> 2개 제외하고 반복처리
    # print( p ) # 확인
    print( p.text ) # <p> </p> 에 내용물 추출
    # 내용물들을 파일에 작성하기
    file.write( p.text +"\n" )

# 파일 닫기
file.close()


# 실습3 : 웹 페이지의 날씨 정보 크롤링 하기
# 실습준비물 : 네이버의 OOO지역날씨 검색
    # https://search.naver.com/search.naver?query=부평구날씨
    # 한글 깨짐이 정상 : https://search.naver.com/search.naver?query=%EC%9D%B8%EC%B2%9C%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8

# 3-1
url = 'https://search.naver.com/search.naver?query=%EC%9D%B8%EC%B2%9C%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8'

# 3-2
HTMLreq = urllib.request.urlopen( url )

# 3-3
HTMLData = BeautifulSoup( HTMLreq.read() , 'html.parser' )
# print( HTMLData )

# 3-4 특정 class 의 마크업 만 추출
HTMLdiv = HTMLData.find( 'div' , class_='temperature_text' )
# print( HTMLdiv )

# 3-5 내용물(온도) 만 추출
currentTemperature = HTMLdiv.text
print( f'인천 부평구 , {  currentTemperature } ')












