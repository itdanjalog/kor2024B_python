'''
    파이썬으로 스택 구조 구현
    # 함수
        1. 스택 Full 여부 확인 함수
        2. 스택 Empty 여부 확인 함수
        3. 스택 Push 데이터 삽입 함수
        4. 스택 Pop 데이터 삭제 함수
        5. 스택 peek 최상위 위치의 데이터 확인 함수
'''

# 함수란 : 미리 정해진 실행문(코드)들을 구현해서 반복 사용하는 문법
    # 선언/정의:함수만들기 , 호출/사용: 함수호출
    # 매개변수 : 함수호출시 함수안으로 들어오는 값  ,
    # 리턴 : return 함수가 종료될때 함수를 호출했던곳으로 반환하는 값

# [2] Full 체크 함수 선언/정의 : 현재 스택구조에 저장할 자리가 남았는지 체크
def isFull() :
    global SIZE , stack , top # 전역변수
    # 만약에 현재 top 위치가 사이즈 와 같으면
    if top >= SIZE - 1 :   # 인덱스 0부터 사이즈는 1부터
        return True # 자리 없음 , 스택구조에 저장할 빈칸이 없다.
    else :
        return False # 자리 있음 , 스택구조에 저장할 빈칸이 있다.

# [1] PUSH 함수 선언/정의 , data:매개변수
def push( data ):
    global SIZE, stack, top    # 전역변수
    # 유효성검사 : 빈칸이 있는지 체크
    if isFull() : # 자리가 없으면
        print( '>>stack save fail')
        return # 리턴 함으로써 아래 코드는 실행되지 않는다. 함수 종료
    # 스택구조의 최상단 위치 증가
    top += 1
    stack[top] = data

# [4] isEmpty 함수 선언/정의 , 스택구조의 데이터가 모두 비어 있는지 체크
def isEmpty( ) :
    global SIZE , stack , top
    if top == -1 :  # 현재 top 위치가 -1 이면
        return True # 스택구조내 데이터가 모두 비어있다.
    else:
        return False # 스택구조내 데이터가 1개 이상 존재한다.

# [3] POP 함수 선언/정의 , 스택구조의 최상단 위치의 데이터 제거
def pop( ) :
    global SIZE , stack , top
    # 스택구조내 데이터가 비어 있으면
    if isEmpty() :
        print('>> stack delete fail ')
        return # 함수종료 , 아래코드는 실행되지 않는다.
    stack[top] = None # 현재 TOP 위치의 데이터 제거
    top -= 1 # TOP 위치 한칸 내리기

# [5] peek 함수 선언/정의 , 스택구조의 최상단 위치의 데이터 확인
def peek( ) :
    global SIZE , stack , top
    # 만약에 스택이 비어있으면
    if isEmpty() :
        print( '>> stack data empty')
        return None
    return stack[top] # 현재 최상단 위치의 데이터를 함수 호출했던 곳으로 반환























# 전역변수 선언
SIZE = int( input("stack size : ") )   # 1. 스택의 크기를 입력받기
stack = [ None for _ in range(SIZE) ] # 2. 스택[리스트]에 입력받은 크기만큼 None 할당
    # [ 자료 for _ in range( 개수 ) ] : 자료 를 개수 만큼 반복해서 리스트 선언
print( stack )
top = -1 # 3. 스택의 최상단 위치 기억 , 초기는 -1

while True :
    select = int( input(" 삽입(1) 삭제(2) 확인(3) 종료(4) : "))
    if select == 1 :
        print(' ----- PUSH -----')
        data = input('save data : ')
        push( data ) # 직접 정의한 함수를 호출
    if select == 2 :
        print(' ----- POP -----')
        pop()   # 직접 정의한 함수를 호출
    if select == 3 :
        print(' ----- PEEK -----')
        data = peek()
        print( f'>>stack top data : {data}' )
    if select == 4 : break

    print( stack ) # 현재 스택 상황















