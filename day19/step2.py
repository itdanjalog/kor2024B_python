# [2] 삽입 정렬
    # 1. 사람 들의 키/신장 목록
dataList = [ 188 , 162 , 168 , 155 , 158 , 177 , 172 ]
    # 2. 삽입 정렬 함수
def insertSort( dataList ) :
    n = len( dataList ) # 리스트의 길이(총 요소 개수 )
    # i는 1부터 마지막 인덱스 까지
    for i in range( 1 , n ) :
        # j는 i부터 첫번째 인덱스 까지 ( 역순 )
        for j in range( 1  , 0 , -1 ) :
            # j보다 앞에 있는 값이 더 크면 # > 오름차순  # < 내림차순
            if dataList[j-1] > dataList[j] :
                # 스왑
                dataList[j-1] , dataList[j] = dataList[j] , dataList[j-1]
    # for1 종료
    return dataList

print( dataList ) # 정렬전 # [188, 162, 168, 155, 158, 177, 172]
print( insertSort( dataList ) ) # 정렬후 # [155, 158, 162, 168, 172, 177, 188]


