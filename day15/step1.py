#[1] BeautifulSoup 모듈 설치
#[2] 크롤링 관련된 모듈 가져오기
from bs4 import BeautifulSoup
#[3] HTML 파일을 open
file = open( "웹페이지2.html" , encoding="utf-8" )
#[4] BeautifulSoup 객체 생성 # 오픈한 HTML 자료들 읽어오기
htmlObj = BeautifulSoup( file , 'html.parser' )
# print( htmlObj )
#[5] 읽어온 HTML 에서 특정 마크업 추출 하기
result = htmlObj.find('div' )
print( result )
result = htmlObj.select_one('div')
print( result )
print( htmlObj.findAll('div') )
print( htmlObj.select('div' ))
# [6] 추출한 마크업 사이데 자료 추출 하기 #.text #.string
divText = htmlObj.select_one('div').text #  여기에 크롤링 하세요.[1]
print( divText )
divText2 = htmlObj.find( 'div' ).string
print( divText2 )
# [7] 마크업이름 이 아닌 마크업이 가진 속성 class , id 가지고 식별하기
divText3  = htmlObj.find( 'div' , class_='box1') # box1 이라는 마크업은 없다.
print( divText3 ) # None
divText4 = htmlObj.select_one('.box1')
print( divText4.string ) # <div class="box1"> 여기에 크롤링 하세요.[2] </div>
divText5 = htmlObj.select_one('#box2') # box2 이라는 마크업은 없다.
print( divText5 ) # <div id="box2"> 여기에 크롤링 하세요.[3] </div>
