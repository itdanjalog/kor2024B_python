# https://github.com/itdanjalog/tj_2024A_python/blob/master/src/day01/5_%EB%AC%B8%EC%9E%90%EC%97%B4%ED%95%A8%EC%88%98.py
'''
    csv : 데이터 를 쉼표(,)로 구분 하여 저장 하는 텍스트 파일 형식
        - 데이터 분석 , 데이터 공유 , 데이터 가공 등등 주로 사용 된다.

    파이썬 리스트 : [ ]
        - [ 요소1 , 요소2 , 요소2 ]
        - 2차원 리스트 : [  [  요소1 , 요소2 , 요소3 ] , [  요소1 , 요소2 , 요소3 ] ]
            - 리스트의 첫번째 요소가 1행/줄
            - 리스트의 두번째 요소가 2행/줄

    파이썬 csv 파일 다루기
        [ [1행]  , [2행] , [3행] ]
        [ [열1,열2,열3] , [열1,열2,열3] , [열1,열2,열3] ]
        1. import csv
            - csv 관련된 메소드 제공
        2. file 객체 생성
            open( '파일명.csv' , 'w' )
                w : 쓰기모드
                r : 읽기모드
                newline="" : 새로운 줄바꿈 추가하지 않는다.
        3. csv 쓰기
            csv.writer( 파일객체 , delimiter=',' )
                delimiter : 요소 들의 구분 기준
        4. csv 파일 내보내기
            .writerows( 데이터 )

        5. csv 읽기
            csv.reader( 파일객체 )

    파이참 csv 파일 열기
        - 해당 파일을 오른쪽 클릭 -> 다음에서 열기 -> 탐색기/연결된 애플리케이션 열기
        - 현재 파일이 다른곳에서 열려 있는 상태이면 실행불가. .close()
'''
import csv  # csv 와 관련된 함수들 을 제공

# [1] CSV 파일 쓰기
csvfile = open('file1.csv', 'w', newline="")
contents = csv.writer( csvfile , delimiter=',')
contents.writerows( [ ['유재석',"강호동","신동엽"] , [90,80,70] , [60,80,70] ] )
csvfile.close()

# [2] CSV 파일 읽기
csvfile = open('file1.csv', 'r')
rows = csv.reader( csvfile )
print( rows )   # 읽어온 데이터들을 가지고 있는 객체
print( type(rows) ) # 객체 타입

for row in rows :
    print( type( row ) )    # 하나의 줄/행 을 리스트 타입 으로 반환
    print( row )
    for col in row :        # 하나의 열 을 문자로 타입 으로 반환
        print( type(col) )
        print( col )
csvfile.close()

# 실습1 : 2명의 이름과 전화번호를 입력받아 아래와 같은 형식으로 csv파일로 저장하시오. 실습1.csv
'''
    회원명     전화번호
    유재석     010-0000-0000
    강호동     010-1234-1234
'''
outter = [ ['회원명' , '전화번호'] ]   # 출력할 데이터들의 첫번째 행/줄
name = input( '[1] 회원명 : ')
phone = input( '[1] 연락처 : ')
outter.append( [ name , phone ] )   # 출력할 데이터들의 두번째 행/줄
name = input( '[2] 회원명 : ')
phone = input( '[2] 연락처 : ')
outter.append( [ name , phone ] )   # 출력할 데이터들의 세번째 행/줄

testFile1 = open("testFile1.csv", "w", newline="")
csvOutput = csv.writer( testFile1 , delimiter=',' )
csvOutput.writerows( outter )
testFile1.close()






















