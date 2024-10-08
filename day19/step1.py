# [1] 선택 정렬
    # 1. 사람들의 키/신장 목록
dataList = [ 188 , 162 , 168 , 155 , 158 , 177 , 172 ]
    # 2. 선택 정렬 함수 만들기
def selectSort( dataList ) :
    # 3. 리스트 수 # len( 리스트 ) : 리스트내 전체 요소 수 반환 함수
    n = len( dataList )
    # 4. i=비교기준요소 # i는 0 부터 마지막 인덱스 *전* 까지 반복
    for i in range( 0 , n-1 ) :
        minIndex = i # 최소값이 저장된 인덱스 번호
        # 5. j = 비교대상요소 # j는 비교기준 다음 요소부터 마지막 인덱스 까지 반복
        for j in range( i+1 , n ) :
            if dataList[minIndex] > dataList[j] : # 만약에 최소값이 비교대상보다 더 크면 # > 오름차순  # < 내림차순
                minIndex = j # 최소값를 비교대상으로 변경하기
        # for2 종료 # 비교기준 과 최소값과 위치를 스왑/교체하기
        dataList[i] , dataList[minIndex] = dataList[minIndex]  , dataList[i]
    # for1 종료
    return dataList

print( dataList ) # 정렬 하기전  [188, 162, 168, 155, 158, 177, 172]
print( selectSort( dataList ) ) # 정렬 후 [155, 158, 162, 168, 172, 177, 188]

