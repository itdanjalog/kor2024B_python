# [2] 이진 검색 함수
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


# 이진 검색 함수 (중복 검색 가능)
def binSearchDuplicates(lst, findValue):
    # 리스트가 비어있다면 빈 리스트 반환
    if not lst:
        return []

    pos_list = []  # 검색된 인덱스를 저장할 리스트
    start = 0
    end = len(lst) - 1

    # 이진 검색을 통해 값을 찾음
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == findValue:
            pos_list.append(mid)  # 현재 중간 인덱스 추가

            # 왼쪽으로 탐색하여 중복된 값 찾기
            left = mid - 1
            while left >= 0 and lst[left] == findValue:
                pos_list.append(left)
                left -= 1

            # 오른쪽으로 탐색하여 중복된 값 찾기
            right = mid + 1
            while right < len(lst) and lst[right] == findValue:
                pos_list.append(right)
                right += 1

            break  # 중간 인덱스를 찾았으므로 반복 종료
        elif lst[mid] < findValue:
            start = mid + 1
        else:
            end = mid - 1

    # 정렬된 결과에서 중복된 값의 인덱스 리스트 반환
    return sorted(pos_list)


# 코드 실행
dataList = [188, 162, 168, 120, 50, 150, 177, 105, 150,120]  # 샘플 데이터
dataList.sort()  # 리스트 정렬
print("정렬된 데이터:", dataList)

# 검색할 값을 입력받기
findValue = int(input('검색할 데이터: '))
# 함수 호출
pos_list = binSearchDuplicates(dataList, findValue)

# 결과 출력
if not pos_list:
    print(findValue, '는 검색 결과가 존재하지 않습니다.')
else:
    print(findValue, '는 검색 결과', pos_list, '위치에 존재합니다.')
