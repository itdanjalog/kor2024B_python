# [2] 이진/이분 검색/탐색
def binSearch( list , findValue ) :
    pos = -1 # 검색을 성공 했을때 찾은 데이터의 위치를 저장 하는 변수
    start = 0 # 첫번째 인덱스를 가지는 변수 # 0
    end = len(list)-1 # 리스트내 마지막 인덱스를 가지는 변수 # n
    # start 부터 end 까지 반복하면서 start 가 end 와 작거나 같으면 반복 종료
    while start <= end :
        # while 조건문 :  # 조건 결과가 True 반복문 실행 , False 이면 반복문 종료
        mid = ( start + end ) // 2  # 가운데 인덱스  : 시작인덱스+끝인덱스 더하고 2로 나눈 인덱스
        if findValue == list[mid] : # 만약에 찾을 데이터가 가운데 인덱스의 값과 같으면
            pos = mid   # 찾을값을 찾았다 # pos에 찾은 데이터의 인덱스 대입
            break # 가장가까운 반복문 탈출 키워드
        elif findValue > list[ mid ] : # 만약에 찾을 데이터가 가운데 인덱스의 값보다 크면 ( 오른쪽 이동 )
            start = mid + 1 # 시각점을 mid의 오른쪽으로 이동
        elif findValue < list[ mid ] : # 만약에 찾을 데이터가 가운데 인덱스의 값보다 작으면 ( 왼쪽 이동 )
            end = mid - 1 # 끝점을 mid의 왼쪽으로 이동
    # while 종료 이후
    return pos
# 샘플 데이터
dataList = [ 188 , 162 , 150 , 168 , 155 , 182 , 177 , 172 ]
# 이진/이분 탐색은 정렬이 필수적이다.
dataList.sort() # .sort() : 자동으로 리스트내 요소들이 오름차순으로 정렬 함수
print( dataList ) # [150, 155, 162, 168, 172, 177, 182, 188]
findValue = int( input('검색할 데이터 : '))
pos = binSearch( dataList , findValue ) # 함수호출
if pos == -1 :
    print( f'{ findValue }는 검색 결과 존재 하지 않습니다. ')
else :
    print( f'{ findValue } 는 검색 결과 {pos} 위치에 존재 합니다. ')





















