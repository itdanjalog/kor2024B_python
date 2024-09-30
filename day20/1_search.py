'''
    검색/탐색 : 목록 에서 특정한 값을 찾는 행위
        - 주의 할점 : 정렬이 된 상태 인지 정렬이 안된 상태 인지 확인
        1. 순차 검색 : 목록 에서 순서 대로 저장 되어 있는 자료를 처음 부터 끝까지 순서 대로 검색/탐색 방법
            사용처 : 1. 정렬 없는 상태의 목록 2. 검색 속도 느리다.

        2. 이진/이분 검색 : 목록에서 가운데에 있는 항목을 비교 하여 작으면 왼쪽 , 크면 오른쪽 이진 검색 방법
            사용처 : 1. 정렬 있는 상태의 목록 2. 검색 속도 빠르다.

        3. 이진 트리 검색 : 이진트리( python2 day06)를 이용한 검색 방법

        4. 해싱 검색 : (딕셔너리 python1 day07 ) 키가 있는 위치를 계산하여 바로 값을 찾아가는 방법

    - 함수 : 실행문/코드를 미리 정의 해서 반복적 으로 사용 할때 사용 되는 문법
        - 함수 정의 , 함수 호출
            함수 정의 : 함수를 만드는 행위 , def 함수명( 매개변수1 , 매개변수2 ) :
            함수 호출 : 정의된 함수를 호출/사용 행위 , 함수명( 값1 , 값2 )
        - 매개 변수 : 함수 호출/사용 할때 함수 안으로 들어 가는 값
        - 리턴 값 : 함수 실행 후 함수가 호출 했던 곳으로 반환 되는 값

    - 리스트 : 여러개 데이터를 저장하는 하나의 자료
        - 대괄호 사용 : [ ]
        - [ 요소1 , 요소2 , 요소3 ]
        - 리스트 관련 함수
            - 1. .append( 요소값 ) : 리스트내 요소 추가
'''
# [1] 순차 검색 함수 정의 : for문 활용한 구현 , 매개변수 : 검색할대상의목록=list , 목록에서찾을데이터=findValue
def seqSearch( list , findValue ) : # 매개변수 : 리스트 , 찾을값
    pos = -1 # * 검색 성공 했을때 찾을 데이터의 위치를 저장하는 변수[ -1:못찾았다. 0이상:찾았다 ]
    # 1. 반복문[for] 을 이용한 특정 값 찾기
        # 1-1 리스트내 요소 하나씩 (순회)반복 처리
    #for element in list :
    #    print( element )
        # 1-2 리스트내 요소의 인덱스를 하나씩 (순회) 반복 처리
    for index in range( len( list) ) :
        # print( index )
        # 2. 만약에 특정한 위치의 요소 값이 찾을 데이터 와 같으면
        if list[index] == findValue :
            # 3. 찾은 인덱스 을 pos 변수에 대입
            pos = index
            # 3-2 반복문 종료
            break
    # 4. for 종료되면 post 반환한다. 함수 종료
    return pos

# 코드 실행
dataList = [ 188 , 162 , 150 , 168 , 120 , 50 , 150 , 177 , 105 ] # 샘플 데이터 목록( 150중복 )
# 검색할 데이터
findValue = int( input( '검색할 데이터 : ') )
# 함수 호출/사용
pos = seqSearch( dataList , findValue )
if pos == -1 :
    print( findValue , '의 검색 결과가 존재하지 않습니다.')
else :
    print( findValue , '의 검색 결과는 ', pos ,' 위치에 존재 합니다.')





# [2-2:중복허용 ] 순차 검색 함수 정의
def seqSearchDup( list , findValue ) :
    posList = [ ] # * 검색된 인덱스가 여러개(중복) 저장하기 위한 리스트 선언

    # 1. 매개변수로 받은 리스트 요소의 인덱스를 하나씩 순회 반복처리
    for index in range( len(list) ) :
        # 2. 만약에 index 번쨰의 요소 값과 찾을데이터와 일치하면
        if list[index] == findValue :
            # 3. 검색된 인덱스 목록에 찾은 인덱스를 추가
            posList.append( index )
            # break : break제거하는 이유는 뒤에 동일한 중복값이 존재할수 있으므로
    # 4. for 종료 되면 postList 반환 한다, 함수 종료
    return posList

# 코드 실행
dataList = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ] # 샘플 데이터 목록( 150중복 )
# 검색할 데이터
findValue = int( input( '검색할 데이터 : ') )
# 함수 호출/사용
posList = seqSearchDup( dataList , findValue )
#
if posList == [ ] : #만약에 postList 리스트가 비어 있으면 , 요소가 하나도 없으면
    print( findValue , '의 검색 결과가 존재하지 않습니다.')
else :
    print( findValue, '의 검색 결과는 ', posList, ' 위치에 존재 합니다.')



























