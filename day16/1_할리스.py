# day10 > 3_할리스커피매장.py
# 1. 모듈
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd  # pandas 설치

# [code 1]
def hollys_store( result ) :
    for page in range(1, 51):  # 1 ~ 50까지 반복
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"  # 할리스 매장 정보 url
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup( response, "html.parser");  # print( soup )
        tbody = soup.select_one('tbody'); # print( tbody )
        for row in tbody.select('tr'):
            if len(row)<= 3: break
            tds = row.select('td')
            store_sido = tds[0].string;  # print( store_sido )
            store_name = tds[1].string;  # print( store_name )
            store_address = tds[3].string;  # print( store_address )
            store_phone = tds[5].string;  # print( store_phone )
            store = [store_name, store_sido, store_address, store_phone] # 매장 정보 1개당 리스트 1개
            result.append(store)  # 리스트 안에 리스트 요소 추가 : 2차원 리스트 # [ [ ] , [ ] , [ ], [ ]  ]
# [code 0]
def main() :
    result = []  # 할리스 매장정보 리스트 를 여러개 저장하는 리스트 변수 , 2차원 리스트  # [ [ ] , [ ] , [ ], [ ]  ]
    print(" >>>> 할리스 매장 크롤링 중 >>>>")
    hollys_store( result )
    print( result )

if __name__ == "__main__" :
    main()