'''
    정렬(sort) : 데이터/자료 들을 일정한 순서 대로 나열
        - 정렬된 데이터 들은 검색이 빠르다. [ 검색 속도 향상 ]
        - 오름차순 ASC , 내림차순 DESC
            오름차순 : 1 2 3 4 , A B C D , 가 나 다 라 , 07/25 07/26 07/27
            내림차순 : 4 3 2 1 , D C B A , 라 다 나 가 , 07/27 07/26 07/25
        - 종류
            1. 선택 정렬 , Selection Sort
                - 여러 데이터들 중에서 가장 작은값/큰값 을 뽑는 과정을 반복하여 값 정렬 방법이다.
                - 최솟 값을 찾아서 순서 대로 배치 => 오름 차순
                - 최댓 값을 찾아서 순서 대로 배치 => 내림 차순
                [ 188 , 162 , 168 , 120 , 50 ]  -가장 작은값 찾아서-->        50
                [ 188 , 162 , 168 , 120 ]       -가장 작은값 찾아서-->        50 , 120
                [ 188 , 162 , 168  ]            -가장 작은값 찾아서-->        50 , 120 , 162
                [ 188 , 168  ]                  -가장 작은값 찾아서-->        50 , 120 , 162 , 168
                [ 188 ]                         -가장 작은값 찾아서-->        50 , 120 , 162 , 168 , 188

                - 교환 정렬
                    - swap : 두 변수의 값 교체 하기
                        - 두 변수가 가지고 있는 값을 서로 바꿔 치기
                        a = 3
                        b = 5
                        -----
                    -- 일반적인 방법 1
                        temp : 임시 변수
                        1. temp = a     -- 임시변수에 3를 대입하고
                        2. a = b        -- a변수에 5를 대입하고
                        3. b = temp     -- b변수에 temp(3) 를 대입하고
                        a = 5 , b = 3
                    - 파이썬 문법 방법 2
                        a , b = b , a
                        a = 5 , b = 3

            2. 삽입 정렬 , Insertion sort
                - 기존 데이터들 중에서 자신의 위치를 찾아서 데이터를 삽입/교환 하는 정렬

            3. 버블 정렬 , Bubble sort
                -
            4. 퀵 정렬 , Quick sort
            등등
'''
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

# [2] 교환 정렬
    # 1. 정렬 전 리스트
dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
    # 교환 정렬 함수 정의
def swapSort( list ) : # 1. 함수 정의 , 매개변수로 리스트를 받는다.
    n = len(list)       # 2. 리스트의 길이 변수
    for i in range( 0 , n-1 ) : # 3. i는 0부터 마지막 인덱스 까지 반복 처리
        print( '비교기준 : ' , list[i] )
        minInx = i              # 4. 가장 작은 데이터의 인덱스 위치를 저장하는 변수
        for j in range( i+1 , n ) : # 5. 다음 값부터 마지막 값까지 반복문
            if list[minInx] > list[j] : # 6. 현재 최솟값이 다음 j 번째 인덱스 값보다 크면
                minInx = j # 7. 현재 최솟값 인덱스를 j번째 인덱스로 대입/수정
            print('>>비교대상 : ' , list[j] )

        print( '>>>>>가장 작은 값 : ', list[minInx] )
        # i번째 값과 최솟값의 위치를 서로 바꾸기
        # swap(교체 방법1)
        temp = list[i]
        list[i] = list[minInx]
        list[minInx] = temp
        # swap(교체 방법2)
        # list[i] , list[minInx] = list[minInx] , list[i]
    return list

print( '정렬 후 기존 리스트 : ' , dataList )
print( '정렬 후 리스트 : ' , swapSort( dataList ) )






















