# [4] 파이썬을 이용한 큐 구조 구현 활용
'''
    큐 구조 기능 구현
    1. isFull() : 큐가 다 찾는지 확인 함수
    2. isEmpty() : 큐가 다 비어 있는지 확인 함수
    3. peek() : 가장 앞에 위치에 데이터 확인 함수
    4. enQueue : 큐에 데이터를 삽입 함수
    5. deQueue : 큐에 데이터를 삭제 함수
'''
# 1. isEmpty() 함수 구현
def isEmpty() :
    global SIZE ,queue , front , rear # 전역변수를 함수 안으로 가져온다.
    if front == rear : # 만약에 front , rear 위치가 같으면
        return True # 큐가 다 비어 있다는 뜻 . # front:출구 rear:입구 # 입구와출구가 같은 위치이기 때문에
    else :
        return False

# 2. deQueue() 함수 구현 # 큐 구조내 데이터 삭제 함수
def deQueue( ) :
    global SIZE ,  queue , front , rear
    if isEmpty() :  # 만약에 비어 있으면 삭제 불가능하다.
        return  #함수 강제 종료  # 큐가 다 비어 있다.
    # 데이터  삭제한다.
    front += 1 # 1증가
    queue[front] = None # 지정한 위치에 값 덮기

# 3.
def peek () :
    global SIZE , queue , front , rear
    if isEmpty() : # 만약에 비어 있으면 확인 불가능
        return None
    return queue[ front + 1 ]

# 4. isFull() 함수
def isFull( ) :
    global SIZE , queue , front , rear
    if rear != SIZE-1 : # 현재 rear 위치가 전체 크기와 같지 않으면
        return False # 빈칸이 존재 했을때 False
    # 만약에 입구가 최대크기와 같고 출구가 가장 뒤에 위치하면
    elif rear == SIZE -1 and front != -1 :
        return True # 빈칸이 존재하지 않을때 True # 빈칸이 없다.
    else : # 그외 남아 있는 데이터들을 한칸씩 앞으로 당기기
        for i in range( front + 1 , SIZE ) :
            queue[ i - 1 ] = queue [ i ]
            print( queue )
            # 앞전 데이터가 위치했던곳에 새로운 데이터를 대입한다.
        queue[SIZE - 1] = None  # 마지막 자리는 None으로 설정
        # for end
        front -= 1
        rear -= 1
        return False

# 5. enQueue( ) 함수
def enQueue( data ) :
    global SIZE , queue , front , rear
    if isFull() :  # 만약에 다 찼으면
        return None
    rear += 1 # 입구 1증가
    queue[rear] = data # rear 위치에 데이터 대입

######################################################################
SIZE = int(input('queue size : '))  # 1. 큐의 크기를 입력받기
queue = [ None for _ in range(SIZE) ] # 2. 큐의 크기만큼 리스트 선언
front = -1 #3. 큐의 출구 위치 기억변수
rear = -1 #4. 큐의 입구 위치 기역변수

while True : # 5.무한루프
    print( front , rear )
    print( queue ) # 큐 내부 확인
    select = int( input(' 1.삽입 2.삭제 3.확인 4.종료') )
    if select == 1 :
        newData = input('save data : ')
        enQueue( newData )
    if select == 2 :
        deQueue()
    if select == 3 :
        data = peek()
        print( data )
    if select == 4 :
        break # 가장 가까운 반복문을 강제 종료 및 탈출