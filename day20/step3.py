# 실습1 : 순차검색과 이진검색 중 성능차이
# 1. 난수 100만개 생성 하고 생성된 난수를 저장된 배열 생성
# 2. 순차검색(비정렬) 이용한 검색
# 3. 순차검색( 정렬 ) 이용한 검색
# 4. 이진검색( 정렬필수 ) 이용한 검색
import random # 난수 모듈 호출 하기
# 순차검색 함수
def seqSearch( list , findValue ) :
    pos = -1
    global count # 함수 밖에 있는 전역변수를 함수 안에서 사용하기 위해 호출하는 키워드
    for index in range( len(list) ) :
        count += 1 # 검색횟수 1씩 증가
        if list[index] == findValue  :
            pos = index
            break
    return pos

# 이진/이분 검색 함수
def binSearch( list , findValue ) :
    start = 0
    end = len(list) -1
    global count
    while start <= end : # 시작점이 끝점보다 작거나 같을때 까지 무한반복
        count += 1 # 탐색횟수 1증가
        mid = ( start + end ) // 2 # 가운데 인덱스
        if list[mid] == findValue :
            return mid
        elif list[mid] < findValue : # 찾는값이 가운데값보다 더크면
            start = mid + 1 # 오른쪽으로 이동
        else : # 찾는값이 가운데값보다 더 작으면
            end = mid - 1 # 왼쪽으로 이동
    return -1 # 못찼으면 -1 반환하기

# 1. 난수생성 # 0 ~ 1000000 중 난수 생성하여 100만개 를 저장하는 리스트 선언
dataAry = [ random.randint( 0 , 1000000 ) for _ in range(1000000) ]
# print( dataAry ) # 100만개의 숫자가 들어있는 리스트

# 2. 순차검색을 하여 100만개 중에 9000 이라는 데이터 검색/탐색
count = 0
pos = seqSearch( dataAry , 9000 )
print( f'{ pos } , { count }회')

dataAry.sort() # .sort() : 리스트 정렬함수
# 3. 정렬된 순차검색을 하여 100만개 중에 9000 이라는 데이터 검색/탐색
count = 0
pos = seqSearch( dataAry , 9000 )
print( f'{ pos } , { count }회') # 결론] 순차검색은 목록에 정렬이 없어도 가능하지만 정렬된 데이터가 훨씬 더 좋은 성능을 가진다.

# 4. 정렬된 이진검색을 하여 100만개 중에 9000 이라는 데이터 검색/탐색
count = 0
pos = binSearch( dataAry , 9000 )
print( f'{ pos } , { count }회')
