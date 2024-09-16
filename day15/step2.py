'''


'''

# 1. 크롤링에 필요한 라이브러리 설치한다.
# 2. 설치된 라이브러리의 기능(함수)를 해당 py 파일의 호출한다
from bs4 import BeautifulSoup
# 3. HTML 파일를 읽어드리고 HTML분석객체 반환
HTMLData = BeautifulSoup(  open("2_웹페이지크롤링.html" , encoding="utf-8") , "html.parser" )
# 5. 확인
print("\n>>(5) 2_웹페이지크롤링.html 읽은 내용 ")
print( HTMLData )   # 모든 HTML 문법이 (문자열형태로) 출력된다.
# 6. 특정 마크업 만 검색/조회 하기
    # HTML객체.find( '호출할마크업명' )
HTMLdiv = HTMLData.find( 'div' )
print("\n>>>>(6)  html 내 div 마크업 찾기 ")
print( HTMLdiv )# 확인
# 7. 특정 마크업의 마크업을 제외한 내용만 검색/조회 하기
HTMLcontent = HTMLData.find( 'div' ).text
print("\n>>>>(7)  html 내 div 마크업의 내용물 ")
print( HTMLcontent )
# 8. 특정 마크업 만 검색/조회 해서 여러개 가져오기
    # HTML객체.find_all( )
HTMLdivs = HTMLData.find_all( 'div' )
print("\n>>>>(8)  html 내 div 마크업 여러개 찾기(리스트 로 반환) ")
print( HTMLdivs )
# 9. 반환된 리스트를 반복문 처리
for div in HTMLdivs :
    print( div )
# 10. 특정한 class 명을 검색/조회 해서 가져오기
    # .find( '마크업명' , class_='클래스명' )
HTMLbox1 = HTMLData.find( 'div' , class_="box1" )
print("\n>>>>(10)  html 내 div 마크업의 특정 class 호출하기 ")
print( HTMLbox1 )
# 11 . 특정한 id 명을 검색/조회 해서 가져오기
    # .find( '마크업명' , id = 'id명' )
HTMLbox2 = HTMLData.find( 'div' , id = "box2" )
print("\n>>>>(11)  html 내 div 마크업의 특정 id 호출하기 ")
print( HTMLbox2 )



