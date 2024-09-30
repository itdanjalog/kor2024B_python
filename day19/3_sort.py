

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








# [5] 퀵 정렬
    # - 기준[pivot] 을 선정 하는 첫 과정 , 첫 기준은 중간에 있는 인덱스 값
    # 기준으로 작은값은 왼쪽 , 큰값은 오른쪽 배치
    # 데이터가 많으면 많을수록 다른 정렬보다 정렬속도가 빠르다.

dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ] # 데이터 샘플

def quickSort( list ) :
    n = len( list )
    if n <= 1 : # 만약에 길이가 1보다 작거나 같으면 종료하고 리스트 반환
        return list
    pivot = list[ n//2 ] # 리스트 내 가운데 인덱스 를 첫 기준 으로 선정
        # 길이가 홀수 이면    길이가 7 이면  7//2 --> 3.5 --> 3
        # 길이가 짝수 이면    길이가 7 이면  8//2 --> 4 --> 4

    left = [ ]  # 기준보다 작은 데이터들
    right = [ ] # 기준보다 큰 데이터들

    for i in list : # 리스트에 요소 하나씩 꺼내기
        if i < pivot : # i번쨰 값이 기준보다 작으면
            left.append( i )
        elif i > pivot : # i번째 값이 기준보다 크면
            right.append( i )
    # print( 'list 원본 : ' , list )
    # print( '기준 : ' , pivot )
    # print( '재귀 하기 전 list left : ' , left  )
    # print( '재귀 하기 전 list right : ', right )
    # !!!! 핵심 : 재귀함수
    return quickSort( left ) + [ pivot ] + quickSort( right )

print( quickSort( dataList ) )



















