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