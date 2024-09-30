''' 2_search.py

    이진/이분 검색

    - 반복문
        1. for문
            - for 반복변수 in range( ) :
            - for 반복변수 in 리스트 :
            등등
        2. while문
            - 조건식이 True 이면 반복문 처리 하고 False 이면 반복문 종료
            - while 조건식 :

'''
# [1] 이진 검색 함수
def binSearch( list , findValue ) :
    # 검색 성공 했을때 찾을 데이터 의 위치를 저장 하는 변수
    pos = -1
    # 시작 인덱스 변수
    start = 0           # 첫번째 인덱스 를 가지고 검색 시작
    # 끝 인덱스 변수
    end = len(list)-1   # 마지막 인덱스 가지고 검색 시작
    # start 부터 end 까지 반복 처리 , start 가 end 와 작거나 같으면  반복문 종료
    while start <= end :
        # 가운데 인덱스 , 시작인덱스 + 끝인덱스 // 2
        mid = ( start + end ) // 2
        # 만약에 찾을 데이터가 가운데 인덱스의 값과 같으면
        if findValue == list[mid] :
            pos = mid       # pos변수에 찾은 인덱스 대입
            break           # 반복문 종료
        # 아니고 찾을 데이터가 가운데 인덱스의 값보다 더 크면
        elif findValue > list[mid] :
            # 시작점을 mid의 오른쪽으로 이동
            start = mid + 1
        # 아니고 찾을 데이터가 가운데 인덱스의 값보다 더 작으면
        elif findValue < list[mid] :
            # 끝점을 mid의 왼쪽으로 이동
            end = mid -1
    # while 반복문 종료되고 함수 종료
    return pos




# 코드 실행
dataList = [188, 162, 168, 120, 50, 150, 177, 105]  # 샘플 데이터
# 리스트 정렬
    # .sort() : 리스트내 요소들을 오름차순 정렬 함수 ( 제공 되는 정렬 함수 )
dataList.sort( )
print( dataList )
# 검색할 값을 입력받기
findValue = int( input('검색할 데이터 : ') )
# 함수 호출
pos = binSearch( dataList , findValue )
# 결과
if pos == -1 :
    print( findValue,'는 검색 결과 존재 하지 않습니다. ')
else :
    print( findValue,'는 겸색 결과 ', pos ,' 위치에 존재 합니다.')












