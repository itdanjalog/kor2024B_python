# 1. 모듈 가져오기
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json


bookName = [ '001001009'  , '001001003' , '001001025' ]
# [1] 쿠우쿠우 매장 정보 크롤링 서비스
def qooqooStoreInfo( result ) :

    for page in bookName :
        print(f'---------------------------{page}------------------------------')
        # 2. 지정한 url 를 호출해서 응답 받기
        url = f"https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=10&categoryNumber={page}"
        response = urllib.request.urlopen( url )
        if response.getcode() == 200 :
            print('>> 통신 성공')
            # 3. 통신 응답 결과를 읽어 와서 크롤링 파싱 준비
            soup = BeautifulSoup( response.read() , "html.parser" ); # print( soup )
            # 4. 분석한 HTML 식별자들을 파싱 , find , findall , select , select_one
            #print( soup )

            tbody = soup.select_one('#yesBestList'); # print( tbody )  # 4-1 테이블 전체 파싱
            #print( tbody )
            rows = tbody.select('li'); # print(rows) # 4-2 테이블(전체매장) 마다 행(매장) 파싱
            for row in rows :  # 4-3 행(매장) 마다
                #print( row )
                cols = row.select('.itemUnit > .item_info > .info_name > .gd_name');
                #print( cols ) #  4-3 열(각매장정보) 파싱
                #cols2 = cols.select_one('.info_name');
                #print( cols2 )
                #title = cols2.select_one('a')
                #print( title.string )
                # # 모바일 행 제외
                if len( cols ) < 1 : # 만약에 열이 개수가 1개이면 모바일 이라고 가정해서 파싱 제외
                    continue # 가장 가까운 반복문으로 이동 , 아래 코드는 실행되지 않는다.
                print( cols[0].string , end='\t\t\t' )

                cols = row.select('.itemUnit > .item_info > .info_pubGrp > .info_auth > a');
                # print( cols )

                for i in cols :
                    print( i.string , end="," )

                print()


                # # 각 정보들을 파싱 , *공백 제거
                # 번호 = cols[0].string.strip()
                # 지점명 = cols[1].select('a')[1].string.strip() # 2번째 열의 2개 a가 존재하는데 2번째 a태그의 텍스트를 파싱
                #연락처 = cols.select_one('a').string.strip()
                #print( 연락처 )
                # 주소 = cols[3].select_one('a').string.strip()
                # 영업시간 = cols[4].select_one('a').string.strip()
                #
                # # 5. 파싱한 정보를 리스트에 담기
                # 매장 = [ 번호 , 지점명 , 연락처 , 주소 , 영업시간 ] # print( 매장 ) # 리스트 에 담기 ( 왜? df 사용하기 위해서 2차원 리스트 구성할 예정 )
                # result.append( 매장 ) # 리스트에 파싱한 리스트 담기 # 2차원 리스트
        else :
            print('>> 통신 실패 ')
    # 7. 리스트 반환
    return result

if __name__ == "__main__" :
    result = []
    qooqooStoreInfo( result ); print( result ); # 쿠우쿠우 매장 정보 크롤링 서비스 호출
