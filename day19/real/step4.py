dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]  # 데이터 샘플
# [4] 버블(교환) 정렬
    # - 첫번째 값부터 시작해서 바로 앞뒤 데이터를 비교하여 큰 것은 뒤로 보내는 방식
def bubbleSort( list ) :
    n = len(list)
    for i in range ( n-1 , 0 , -1 ) :   # 뒤
        print( i , list[i]  , " Scan ----------------> " , list )
        changeCheck = False # 교환/스왑 여부 확인 변수 , False 교환 안했다는 뜻
        for j in range( 0 , i ) :       # 앞
            print( j , list[j]  )
            if list[j] > list[ j+1 ] :
                # 스왑
                list[j] , list[j+1] = list[j+1] , list[j]
                changeCheck = True # 만약에 교환 했으면 True 변경 , True 교환 했다는 뜻
                print( '>> 스왑 처리 ')
                print( '>>>>>> ' , list )
        if changeCheck == False : # 만약에 한번도 교환을 안했으면
            break # 정렬이 완료된 상태이므로 반복문 종료
    return list

print( bubbleSort( dataList ) )
print( '-------------------------------------- 구분선 --------------------------------------')

