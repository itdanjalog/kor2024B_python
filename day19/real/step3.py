# [3] 삽입 정렬
dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
    # 길이 : 1부터 시작 , 인덱스 : 0부터 시작 , 길이와 인덱스 1 차이가 있다.

# 삽입(교환)정렬 함수
def insertSort( list ) :    # 0.함수정의 , 매개변수는 리스트
    n = len( list )           # 1. 리스트의 길이 변수
    for i in range( 1 , n ) : # 2. 두번째 인덱스 부터 마지막 인덱스 까지 반복 처리
        for j in range(  i , 0 , -1 ) : # 3.  i번째 인덱스부터 0번인덱스까지 역순으로 순회
            if list[ j-1 ] > list[ j ] : # 4. 역순 값이 더 크면
                # 스왑 : 두 변수의 값을 바꾸기
                list[ j-1 ] , list[j] = list[j] , list[j-1]
    return list

print( insertSort( dataList ))

