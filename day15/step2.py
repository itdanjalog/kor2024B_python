# [1] url 읽어 오는 모듈
import urllib.request
# [2] 지정한 url 자료 가져오기 # response = urlopen('가져올URL주소')
response = urllib.request.urlopen('https://v.daum.net/v/20240924120601745')
# print( response ) # <http.client.HTTPResponse object at 0x00000294118043D0>
# [3] 가져온 자료 읽어서 변수에 저장 # .read()
htmlData = response.read()
# print( htmlData )
# [4] 읽어온 자료를 bs4 객체로 파싱
from bs4 import BeautifulSoup
soup = BeautifulSoup( htmlData , 'html.parser' )
# [5] 특정 마크업 추출
    # 1. 다음 웹페이지 기사의 제목 추출
    # <h3 class="tit_view" data-translation="true">지금도 소름... 설악산에 밤새 머문 그가 목격한 것</h3>
    # 방법1
print( soup.select('h3') )      # h3 마크업들을 모두 추출해서 리스트 반환
print( soup.select('h3')[0] ) # 반환된 리스트중에 제목이 첫번째 인덱스에 있으므로 [0] 인덱스 추출
print( soup.select('h3')[0].string ) # 마크업을 제외한 내용물만 추출
    # 방법2
print( soup.select_one('.tit_view').string ) # .tit_view # 동일한 클래스명을 가진 마크업을 찾아서 추출
    # 2. 기자 명 추출
    # <span class="txt_info">정윤영</span>
print( soup.select('.txt_info') )
print( soup.select('.txt_info')[0].string ) # 정윤영   # 기자명
print( soup.select('.txt_info')[1].string ) # 2024. 9. 24. 12:06 # 기사날짜

# 실습 : 네이버에서 부평구 날씨 크롤링
지역 = '부평구'
키워드 = 지역+'날씨'   # 부평구날씨
인코딩된키워드 = urllib.parse.quote(키워드) # 지정한 키워드를 인코딩하기 # 웹주소에 한글 사용시 필수
크롤링주소 = 'https://search.naver.com/search.naver?query=' + 인코딩된키워드 # 네이버 검색 주소 와 인코딩된 키워드 연결
# print( 크롤링주소 ) # 확인
#[1] 지정한 url 의 자료 가져오기
response = urllib.request.urlopen( 크롤링주소 )
#[2] 자료 읽어 드리기
htmlData = response.read()
#[3] html 객체로 파싱
soup = BeautifulSoup( htmlData , 'html.parser' )
#[4] 특정한 마크업 내용물 추출
    # 1. 온도 추출
    # <div class="temperature_text"> <strong><span class="blind">현재 온도</span>17.0<span class="celsius">°</span></strong> </div>
print( soup.select_one( '.temperature_text') )
print( soup.select_one( '.temperature_text').text ) #  현재 온도17.0°
    # 2. 습도 추출
    # <dl class="summary_list"> <div class="sort"> <dt class="term">체감</dt> <dd class="desc">19.5°</dd> </div> <div class="sort"> <dt class="term">습도</dt> <dd class="desc">90%</dd> </div> <div class="sort"> <dt class="term">남풍</dt> <dd class="desc">0.7m/s</dd> </div> </dl>
print( soup.select_one('.summary_list') )
print( soup.select_one('.summary_list').select('.sort')[0].text ) # 체감 #  체감 19.4°
print( soup.select_one('.summary_list').select('.sort')[1].text ) # 습도 #  습도 90%
print( soup.select_one('.summary_list').select('.sort')[2].text ) # 풍속 #  남풍 0.6m/s













