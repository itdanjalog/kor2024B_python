''' 3_search.py
    실습1 : 순차 검색 이용한 수 찾기
    실습2 : 이진 검색 이용한 수 찾기
        조건1 : N개의 난수 목록이 주어져 있을때 , 이 안에 M 라는 정수가 존재 하는지 체크 하시오.
        조건2 :
            1. N의 자연수 입력
            2. N개 만큼의 난수 생성
            3. 검색할 M 의 자연수 입력
            4. N개의 난수 목록 중에 M이 존재 하면 1 출력 하고 존재 하지 않으면  0 출력
'''

import random
'''
# 실습1 : 순차 검색
def solution1( list , fdata ) : # 매개변수 : 목록 , 찾을 대상
    # 순차 검색 구현
    for index in range( len(list) ) :
        if list[index] == fdata :
            return 1
    return 0

N = int( input() )  # 1. N의 자연수 입력
dataList = [ random.randint( 1 , 100 ) for _ in range( N ) ] # 2. N개 만큼의 난수 생성
print( dataList )

M = int( input() ) # 3. 검색할 M 의 자연수 입력
print( solution1( dataList , M ) ) #4. N개의 난수 목록 중에 M이 존재 하면 1 출력 하고 존재 하지 않으면  0 출력
'''

# 실습2 : 이진 검색
def solution2( list , fdata  ) : # 매개변수 : 목록 , 찾을대상
    # 이진 검색 구현
    start = 0               # 목록의 시작 인덱스
    end = len( list ) - 1   # 목록의 마지막 인덱스
    # 반복문
    while start <= end : # start가 end 보다 작거나 같으면 검색(반복) 종료
        mid = (start+end) // 2 # 중간 인덱스
        if list[mid] == fdata : # 중간인덱스의 위치한 요소의 값과 찾을대상 값과 같으면
            return 1 # 찾았으면 반환 1
        elif list[mid] < fdata : # 찾을대상이 더 크면
            start = mid + 1 # 시작인덱스를 중간인덱스의 +1 만큼 오른쪽으로 이동
        elif list[mid] > fdata : # 찾을대상이 더 작으면
            end = mid - 1   # 끝인덱스를 중간인덱스의 -1만큼 왼쪽으로 이동
    # 반복문 종료 되었을때 못 찾았으면 0 반환
    return 0

N = int(input()) # 1. N의 자연수 입력
dataList = [random.randint(1, 100) for _ in range(N)] # 2. N개 만큼의 난수 생성

print( dataList ) # 정렬 전 목록
# 정렬 : 이진 검색은 정렬된 목록 에서 효율 적인 검색를 할수 있다.
dataList.sort()
print( dataList ) # 정렬 후 목록

M = int(input()) # 3. 검색할 M 의 자연수 입력
print( solution2( dataList , M) ) # 4. N개의 난수 목록 중에 M이 존재 하면 1 출력 하고 존재 하지 않으면  0 출력














