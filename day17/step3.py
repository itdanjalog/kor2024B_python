'''
    파이썬으로 큐 구조 구현
        1. isFull : 큐가 다 찾는지 확인 함수
        2. isEmpty : 큐가 다 비어 있는지 확인 함수
        3. enQueue : 큐에 데이터 삽입 함수
        4. deQueue : 큐에 데이터 삭제 함수
        5. peek    : 가장 앞에 위치에 데이터 확인 함수
'''

#[2] isFull 함수 선언/정의 : 큐가 다 찾는지 확인 함수
def isFull( ) :
    global SIZE , queue , front , rear
    if rear != SIZE -1 : # 현재 rear 위치가 사이즈와 같지 않으면
        return False # 빈칸이 존재 했을때 False
    elif rear == SIZE -1 and front == -1 :  # 현재 rear 위치가 사이즈와 같고 front 위치가 최하단 이면
        return True # 빈칸이 존재 하지 않을때 True
    else : # 남아 있는 데이터들을 한칸씩 앞으로 당기기
        # 가정 : # [ None , '유재석' , '신동엽' ]
        for i in range( front + 1 , SIZE ) :
            queue[ i - 1 ] = queue[ i ]
            # None = 유재석        # None = 신동엽
            queue[ i ] = None
            # 유재석 = None        # 신동엽 = None
            # 1회전 : [ '유재석' , None , '신동엽' ]
            # 2회원 : [ '유재석' , 신동엽 , None ]
        front -= 1  # front 한칸 뒤로 보내기
        rear -= 1   # rear 한칸 뒤로 보내기
        return False

# [4] isEmpty 함수 선언/정의
def isEmpty( ) :
    global SIZE, queue, front, rear
    if front == rear : # front , rear 같은 위치이면
        return True  # 큐가 다 비어 있다.
    else:
        return False # 큐가 비어 있지 않다.

# [3] deQueue 함수 선언/정의
def deQueue( ) :
    global SIZE, queue, front, rear
    if isEmpty() :
        print( '>>queue delete fail')
        return
    front += 1  # front 1 증가
    queue[front] = None # front위치 데이터 삭제

# [5]
def peek() :
    global SIZE, queue, front, rear
    if isEmpty() :
        print('>>queue data empty')
        return None
    return queue[front + 1]

#[1] enQueue 함수 선언/정의 : 매개변수 를 큐에 저장
def enQueue( data ) :
    global SIZE , queue , front , rear
    if isFull() :
        print('>> queue save fail ')
        return
    # 매개변수를 큐에 저장
    rear += 1 # rear 1 증가
    queue[rear] = data # rear 위치에 값 넣기


# 전역변수 선언
SIZE = int( input("queue size : ") )    # 1. 큐에 사이즈를 입력받는다.
queue = [ None for _ in range(SIZE) ]   # 2. 입력받은 사이즈만큼 리스트[큐] 선언
front = -1  # 나가는 값 위치 기억
rear = -1   # 들어오는 값 위치 기억

while True :
    select = int( input(" 삽입(1) 삭제(2) 확인(3) 종료(4) : "))
    if select == 1 :
        print(' ----- enQueue -----')
        data = input('save data : ')
        enQueue( data )

    if select == 2 :
        print(' ----- dnQueue -----')
        deQueue()

    if select == 3 :
        print(' ----- PEEK -----')
        data = peek()
        print( data )
    if select == 4 : break

    print( queue ) # 현재 큐 상황





