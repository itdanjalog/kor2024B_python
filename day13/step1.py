
import csv  # csv 와 관련된 함수들 을 제공

# [1] CSV 파일 쓰기
csvfile = open( 'test1.csv' , 'w' , newline="" )
contents = csv.writer( csvfile , delimiter=',')
contents.writerows( [ ['유재석',"강호동","신동엽"] , [90,80,70] , [60,80,70] ] )
csvfile.close()

# [2] CSV 파일 읽기
csvfile = open( 'test1.csv' , 'r' )
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

testFile1 = open( "test2.csv" , "w" , newline="" )
csvOutput = csv.writer( testFile1 , delimiter=',' )
csvOutput.writerows( outter )
testFile1.close()





















