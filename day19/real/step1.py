#[1] 선택 정렬
    # 1. 정렬 전 리스트
dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
    # 2. 정렬 후 리스트
sortList = [ ]

    # 최소값 위치 찾는 함수 구현
def findMinIdx( list ) :        # 1. 함수 정의 , 매개변수 : 최솟값 찾을 리스트
    minIdx = 0                  # 2. 최솟값 의 인덱스를 저장하는 변수 , 첫번째 인덱스가 가장 작은 인덱스로 초기화
    for i in range( 1 , len(list) ) : # 3. 두번째 인덱스 부터 마지막 인덱스 까지 반복문
        if list[minIdx] > list[i] :     # 4. 현재 최솟값 이 i번째 인덱스 의 값보다 크면
            # > : 오름차순 , < : 내림차순
            minIdx = i  # 5. 최솟값 의 인덱스위치 를 i번째 인덱스 로 교체/변경/대입
    return minIdx   # 6 반복문 종료 후 가장 작은 데이터 의 인덱스 위치 반환

print( '정렬 전 기존 리스트 : ' , dataList )
print( '정렬 전 새로운 리스트 : ' , sortList )

    # 정렬 실행
for _ in range( len(dataList) ) :           # 1. 리스트의 개수만큼 반복
    minIdx = findMinIdx( dataList )          # 2. findMinIdx함수에 리스트를 매개변수로 대입 하고 최소값의 인덱스위치 반환받는다.
    sortList.append( dataList[minIdx] )     # 3. 새로운 리스트에 최솟값의 인덱스위치 값을 저장한다.
    del( dataList[minIdx] )                 # 4. 기존 리스트에 최솟값의 인덱스를 삭제

print( '정렬 후 기존 리스트 : ' , dataList )
print( '정렬 후 새로운 리스트 : ' , sortList )


'''
    실습1 : 1부터 1000 사이의 난수를 10개 가지는 리스트를 오름차순으로 정렬하기
        - 아래 주어진 코드를 이어서 randomList 를 선택(교환) 정렬 하시오.
'''
import random
randomList = []
for _ in range(10) :
    rand = random.randint( 1 , 1000 )
    randomList.append( rand )
print( randomList )

# 정렬하기
def swapSort( list ) :
    n = len(list) # 1. 리스트의 길이
    # 1. 비교기준 반복문
    for i in range( 0 , n-1 ) :
        minIndex = i
        # 2. 비교대상 반복문
        for j in range( i + 1 , n ) :
            if list[minIndex] > list[j] :
                minIndex = j
        # 2. 비교기준 과 최솟값 인덱스 위치 스왑
        list[i] , list[minIndex] = list[minIndex] , list[i]

    # 3. 모든 비교기준 반복문이 종료되면
    return list

print( swapSort( randomList ))
