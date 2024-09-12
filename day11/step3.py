# [1] 파일 쓰기(생성)
    # 1. 상대경로
open( './test1.txt' , 'w' )
open( '../test2.txt' , 'w' )
    # 2. 절대경로
# 주의사항 : PC 마다의 절대경로는 다르므로 강사와 다르게 본인의 PC경로 로 작성 해주세요.
# open( 'C:/Users/admin/Documents/hyunsu/kor2024B_python/day11/test3.txt', 'w' )

# [2] 파일의 내용 쓰기
file4 = open( './test4.txt' , 'w' ) # 쓰기모드 파일 생성하고 파일객체 반환받아서 변수에 저장
file4.write("python에서 작성한 내용")
file4.close()

file5 = open( './test5.txt' , 'w' , encoding='utf-8')
for value in range( 1 , 11 ) :
    # range( 시작값 , 끝값 ) : 시작값 부터 끝값 전까지 1씩 하는 리스트 반환
    data = f'{ value }번째 줄입니다.\n'
    file5.write( data ) # 파일쓰기
file5.close() # 파일닫기

# [3] 키보드로부터 입력받은 값 을 파일(file6.txt) 에 저장
content = input( 'file content : ')
file6 = open( './test6.txt' , 'w' , encoding='utf-8' )
file6.write( content )
file6.close()

# [4] 파일을 읽는 여러 가지 방법
# 1. .readline()   # 한줄씩 읽어 오는 함수
file = open( './test5.txt' , 'r' , encoding='utf-8' )
line = file.readline( )
print( line )
while True : # 무한반복문
    line = file.readline()
    if not line : # 만약에 읽어온 문자가 '' 공백이면
        break # 가장 가까운 반복문을 종료
    print( line )
file.close() # 파일닫기

# 2. .readlines()   # 모든 내용을 한줄씩 요소로 저장된 리스트 로 반환 함수
file = open( './test5.txt' , 'r' , encoding='utf-8' )
lines = file.readlines()
print( lines )
for line in lines : # for 반복변수 in 리스트 : 리스트내 요소 하나씩 반복변수에 대입반복
    print( line )
file.close() # 파일닫기  # 파일 작업이 끝나면 파일닫기

#3. .read()         # 모든 내용을 읽어 오는 함수
file = open('./test5.txt' , 'r' , encoding='utf-8' )
content = file.read( )
print( content )
file5.close()

# [5] 키보드로부터 입력받은 값이 저장된 (file6.txt) 파일의 자료들을 모두 읽어오기
file = open('./test6.txt' , 'r' , encoding='utf-8' )
conent = file.read( )
print( conent )

# 파일처리 와 예외처리 같이 작성 하기
try : # 1. 파일명의 오타 있거나 존재하지 않는 파일은 예외 발생 # FileNotFoundError
    file = open('./test7.txt' , 'r' , encoding='utf-8')
except FileNotFoundError as e : # 2.예외발생할 경우 안내문구
    print( '존재 하지 않는 파일 이거나 경로의 문제가 있습니다.')
















