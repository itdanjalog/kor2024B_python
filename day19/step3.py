# [3] 버블 정렬
dataList = [ 188 , 162 , 168 , 155 , 158 , 177 , 172 ]
# 버블 정렬 함수
def bubbleSort( list ) :
    n = len(list) # 리스트의 총 요소 수
    # (1)
    for i in range( n-1 , 0 , -1 ) :
        # 교환 여부 확인 변수 # False 교환 안했다는 뜻
        change = False
        #(2)
        for j in range( 0 , i ) :
            if list[j] > list[j+1] :
                # 스왑
                list[j] , list[j+1] = list[j+1] , list[j]
                change = True
        # for2 end # 만약에 한번도 교환을 안했으면
        if change == False :
            break # 정렬이 완료된 상태이므로 전체 반복문 종료
    return list

print( dataList ) # 정렬 전 # [188, 162, 168, 155, 158, 177, 172]
print( bubbleSort( dataList ) ) # 정렬 후 # [155, 158, 162, 168, 172, 177, 188]


