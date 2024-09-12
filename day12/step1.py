# 문자열
# - 문자열 은 리터럴 # 불변성(수정 불가능) 특징
# [1] 파이썬에서 문자열 표현하는 방법 : 1." "  2.' ' 3.""" """ 4.''' '''
a = "코딩도 헤매는 만큼 자기 땅이야"
a = '코딩도 헤매는 만큼 자기 땅이야'
a = """코딩도 헤매는 만큼 자기 땅이야"""
a = '''코딩도 헤메는 만큼 자기 땅이야'''
# [2] 문자열 연산 #   + 연결 , * 배수 , += 연결
print( 'python' + ' is fun' )   # python is fun
print( '=' * 50 )               # ==================================================
a = 'python'
a += ' is fun'
print( a )                      # python is fun
# [3] 문자열 인덱싱 # 문자열내 문자 위치를 인덱스(번호) 표현 # 리스트/튜플
print( 'python'[0] )    # p     # p[0] y[1] t[2] h[3] o[4] n[5]
print( 'python'[2] )    # t
print( 'python'[4] )    # o
print( 'python'[-1] )   # n
print( 'python'[-3] )   # h     # p[-6] y[-5] t[-4] h[-3] o[-2] n[-1]

# [4] 문자열 슬라이싱 # [ 시작번호 : 끝번호(미만) : 증감단위 ]
print( 'python'[ 0 : 2 ] )  # py
print( 'python'[ : 3 ] )    # pyh
print( 'python'[ 2 : ] )    # thon
print( 'python'[ : ] )      # python
print( 'python'[ 2 : -1 ] ) # tho
print( 'python'[ : : 2] )   # pto
print( 'python'[ : : -1] )  # 역순 : nohtyp

# [5] 문자열 관련 함수/기능
    # .(접근/도트)연산자 : "문자열".미리만들어진함수( )

a = '코딩도 헤매는 만큼 자기 땅이야.'
# 1.    .count('찾을문자') # 문자열내 찾을 문자가 존재하면 개수 반환 함수
print( a.count('자') ) # 1 # 지정한 문자열내 '자' 인 문자가 1개 존재 뜻
print( a.count('가') ) # 0 # 지정한 문자열내 '가' 인 문자가 0개 존재 뜻

# 2.    .find('찾을문자')   #문자열내 찾을 문자가 존재하면 찾은문자의 인덱스를 없으면 -1 반환 함수
print( a.find('자') )    # 11    # 문자열내 '자'인 문자의 인덱스 위치
print( a.find('가') )    # -1    # 문자열내 '가'인 문자의 인덱스 없다 는 뜻

# 3.    .index('찾을문자')  # 문자열내 찾을 문자가 존재하면 찾은문자의 인덱스를 없으면 예외발생 하는 함수
print( a.index('자') )   # 11
try : # 예외처리
    print( a.index('가') )   # ValueError: substring not found
except ValueError as e :
    print( e )

# 4.    '특정문자'.join( "문자열" 또는 리스트 )   # 문자열내 또는 리스트 요소 사이의 특정문자를 삽입 해서 (새로운) 문자열 반환 함수
print( ','.join( a ) ) # 코딩도 헤매는 만큼 자기 땅이야. # 코,딩,도, ,헤,매,는, ,만,큼, ,자,기, ,땅,이,야,.
b = [ 'python' , 'java' , 'c' , 'c++' ]
print( ' <=> '.join( b ) ) # python <=> java <=> c <=> c++

c = 'AbCdEf'
# 5.    .upper( )   # 대문자로 치환해서 (새로운) 문자열 반환 함수
print( c.upper() ) #    ABCDEF
print( c )           # AbCdEf   # c는 원본 그대로
c = c.upper()
print( c )           # ABCDEF
# 6.    .lower( )   # 소문자로 치환해서 (새로운) 문자열 반환 함수
print( c.lower() ) #    abcdef

d = '       pyt hon        '    #앞뒤 공백이 많은 문자열
# 7.     .lstrip()  # 문자열내 왼쪽 공백 제거 된 (새로운) 문자열 반환 함수
print( d.lstrip() ) # pyt hon        ;
# 8.    .rstrip()   # 문자열내 오른쪽 공백 제거 된 (새로운) 문자열 반환 함수
print( d.rstrip() ) #        pyt hon;
# 9.    .strip()    # 문자열내 양쪽 공백 제거 된 (새로운) 문자열 반환 함수
print( d.strip() )  # pyt hon;
print( d )          #        pyt hon        ;

# 10. .replace( '기존문자' , '새로운문자' )
# 문자열내 기존문자가 존재하면 새로운문자 로 치환/변경해서  (새로운) 문자열 반환 함수
print( a.replace("코딩" , "파이썬") ) # 파이썬도 헤매는 만큼 자기 땅이야.

# 11.   .split('구분자')  # 구분자 기준 으로  문자열을 분해 해서 리스트 반환
print( a.split(" ") ) # 구분자에 공백 # ['코딩도', '헤매는', '만큼', '자기', '땅이야.']
d = '가:나:다:라'
print( d.split(':') ) # :콜론 기준으로 분해 # 가:나:다:라

# 실습1 : 아래 csvData를 아래 출력 조건과 같이 출력하시오.
'''[출력예시]
    이름      나이
    유재석     39
    강호동     45
    신동엽     21
'''
csvData = """유재석,39\n강호동,45\n신동엽,21"""
str1 = csvData.split('\n')
# print( str1 )           # ['유재석,39', '강호동,45', '신동엽21']
for str2 in str1 : # 'str1' 이라는 리스트 를 반복문 사용하여 하나씩 반복하기
    # for 반복요소 in 리스트 : 리스트내 첫번째 요소부터 마지막 요소까지 반복요소에 대입 반복
    # print( str2 )   # 유재석,39 # 강호동,45 # 신동엽,21
    str3 = str2.split(',')
    # print( str3 )   # ['유재석', '39'] #['강호동', '45'] #['신동엽', '21']
    print( f' { str3[0] } \t { str3[1]} ')  # \t : 들여쓰기[탭]

# 실습2 : 여러명의 이름 과 나이 를 입력 받아서 csv형식으로 저장
# CSV란? 데이터(속성) 를 ,(쉼표) 구분 하고 행 를 \n(줄바꿈) 구분 하는 형식
    # 이름 과 나이 를 구분할때는 ,(쉼표)
    # 사람 과 사람 를 구분할때는 \n(줄바꿈)
personList = '' # 여러명의 사람들 정보를 가지는 문자열 ( csv 형식 )
while True :
    name = input('name : ')
    if name == 'x' :  # 만약에 name 이 'x' 이면 반복문 종료
        break # 가장 가까운 반복문 종료
    age = input('age : ')
    # 문자열 연산
    # person = name + age # 추후에 이름과 나이를 구분하기 힘들다.
    person = name + ',' + age # 이름 과 나이 사이에 , 삽입 해서 구분이 가능하다.
    # 사람 과 사람 구분 해서 사람명단 에 저장
    personList += person +"\n"
# 확인
print( personList )




























