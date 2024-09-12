
'''
    3_file.py
        파일 처리
            - 메모리 : 컴퓨터 의 저장 장치
                1. 주기억 장치       : 현재 실행중인 프로그램의 데이터 저장
                    - 휘발성 메모리 : 전기 없으면 저장이 안된다.
                    -  파이썬 실행 중에 생성된 자료/데이터 들은 파이썬이 종료 되면 모두 사라 진다.

                2. 보조 기억 장치    : 실행 하지 않는 상태의 프로그램의 데이터 저장
                    - 비휘발성 메모리 : 전기 없어도 저장이 가능하다.
                    - .py 파일은 파이참이 종료 되어도 유지된다. 코드는 사라지지 않는다.

        - 사용 목적 : 변수에 저장된 자료의 값,리스트,딕셔너리,객체 등등의 자료들을 영구 저장/기록
            - 파이썬 메모리 외 다른곳[윈도우] 에 저장 하다.

        - 파일 쓰기
            open( '파일명.확장자' , '옵션' , encoding='문자 인코딩' )
            - open() 실행결과는 매개변수의 따라 파일 객체 반환

                - 옵션 :
                    'w' : 새로 쓰기
                    'r' : 파일 내용 읽기
                - encoding : 파일의 인코딩 방식
                    'UTF-8' : 전세계 언어 들을 표현 가능한 인코딩

                - 자주 사용 되는 메소드
                    .write( 출력할데이터 ) : 파일에 작성할 내용을 매개변수에 대입
                    .read()             : 파일내 자료 가져오기
                    .close()            : 현재 사용 중인 파일을 닫기 ( -쓰기 파일 닫지 않으면 파일 읽기가 불가능 )

'''
# [1] 파일 쓰기
writeFile = open('day03FILE.txt', 'w', encoding='UTF-8')
# 같은 패키지 의 메모장 파일 생성 되었다.
# [2] 파일 내 데이터 대입하기
writeFile.write("파이썬에서 작성한 자료\n")
# [3] 입력받은 값을 파일에 저장하기
str = input( 'txt파일에 저장할 내용 : ' )
writeFile.write( str )
# [4] 파일 닫기 / 파일 쓰기 종료
writeFile.close()

# [5] 파일 읽기
readFile = open('day03FILE.txt', 'r', encoding='UTF-8')
# [6] 파일내 데이터/자료 가져오기
while True :
    inStr = readFile.read( ) # 파일 자료의 한줄씩 읽어오기
    print( inStr )
    if not inStr : # 만약에 읽어온 자료가 없으면
        break   # 반복문 종료
readFile.close() # 파일 읽기 종료

# ============================
noteFile = open('day03Note.txt', 'w', encoding='utf-8')
while True :
    str = input('[종료는 x ,엔터는 줄바꿈] txt 파일에 작성할 내용 : ')
    if str == 'x' :
        break # 가장 가까운 반복문 종료
    str += '\n' # 입력한 자료를 메모장에 쓰기 하기 전에 뒤에 줄바꿈 문자를 추가
    noteFile.write( str )
noteFile.close() # 파일 쓰기 종료
# ============================
fileName = input( '가져올 파일명.확장자 : ')
try :
    noteReadFile = open( fileName , 'r' , encoding='utf-8')
        # 만약에 존재하지 않는 파일명 을 읽어올때 예외 발생한다. FileNotFoundError
    while True :
        str = noteReadFile.read()
        if not str :
            break
        print( str )
except FileNotFoundError as e :
    print( '[파일읽기 실패] 존재하지 않는 파일명 입니다.')






















