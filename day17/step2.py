# [2] 파이썬을 이용한 스택 구조 구현 활용
'''
    구현할 기능 ( * 직접 만들기 )
        1. 스택구조가 isFull 인지 여부 확인 함수
        2. 스택구조내 isEmpty 여부 확인 함수
        3. 스택구조내 push 테이터 삽입 함수
        4. 스택구조내 POP 데이터 삭제 함
        5. 스택구조내 PEEK 최상위 위치의 데이터 확인 함수
'''

# 1. full 함수 # 스택내 모두 차 있는지 확인 함수
def isFull( ) : # 함수 선언/만들기
    global SIZE , stack , Top # 함수내 전역변수를 식별하는 키워드
    # 만약에 현재 top(스택구조내 마지막 위치) 위치가 사이즈와 같으면 # 다 찼으면
    if Top >= SIZE - 1 : # -1 : Top - 인덱스가 0부터 시작하므로
        return True # 함수가 종료되면서 호출했던곳으로 반환되는 값
    else : # 아니면
        return False

# 2. push 함수 # 스택내 자료를 삽입 함수
def push( data ) :
    global SIZE , stack , Top
    #
    if isFull() : # 스택내 모두 차 있으면
        print('자리가 없다.')
        return
    # 스택구조의 Top 한칸 올리기
    Top += 1
    stack[Top] = data

# 3 isEmpty 함수  # 스택내 모두 비어 있는 확인 함수
def isEmpty( ) :
    global SIZE , stack , Top
    if Top == -1 : # -1(인덱스없다는뜻/자료가 없다뜻)
        return True
    else:
        return False

# 4 POP 함수 # 스택내 최상단 위치의 데이터 제거 함수
def pop( ) :
    global SIZE , stack , Top
    if isEmpty() : #비어있으면 삭제 불가능
        return
    stack[Top] = None # 최상단 위치에 데이터를 제거
    Top -= 1 # 한칸 내리기

# 5 PEEK 함수 # 스택내 최상단 위치의 데이터 확인 함수
def peek( ) :
    global  SIZE , stack , Top
    # 만약에 비어있으면 확인 불가능
    if isEmpty() :
        return
    return stack[Top] # 최상단 위치의 데이터 반환

##################################################
# 스택 관련 함수를 활용
# * 함수 밖에서 선언 하면 '전역변수'
SIZE = int( input('stack size : ') ) # 스택 사이즈를 입력받기
stack = [ None for _ in range( SIZE ) ] # SIZE 만큼 개수를 반복하여 리스트 선언
Top = -1 # 현재 스택의 최상단 위치를 저장하는 변수

while True : # 무한루프
    print( stack ) # 확인용
    select = int(input('1.삽입 2.삭제 3.확인 4.종료 : ') )
    if select == 1 : # 입력값이 1이면
        newData = input('save Data : ')
        push( newData ) # 위에서 입력받은 자료를 push함수에 대입한다.
    if select == 2 : # 입력값이 2이면
        pop()
    if select == 3 :  # 입값이 3이면
        data = peek()
        print( f'stack to data : { data }')
    if select == 4 :
        break # 무한루프 종료



















