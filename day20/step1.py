# [1] 순차/선형 검색/탐색
    # 함수정의 : def 함수명( 매개변수1 , 매개변수2 ) :
    # 매개변수란 : 함수호출시 함수 안으로 들어오는 인자값을 저장하는 변수
    # 함수호출 : 내가만든 또는 만들어진 함수를 호출하는 과정 # 인자값이 ---> 매개변수로 전달
# 함수 정의/만들기 # 함수명 : seqSearch # 매개변수 : 1.list 2. findValue
def seqSearch( list , findValue ) :
    # 함수 실행문 정의 : 함수가 실행/호출 될때 실행/처리 되는 코드들
    pos = -1 # 찾은 데이터의 (인덱스)위치를 저장하는 변수 # -1:못찾았다 0이상:찾았다
    # for문 이용한 리스트내 찾을 데이터 찾기
        # for 반복변수 in range( 수 ) : 0 ~ 수 전까지 반복변수에 대입 반복  # len( 리스트 ) : 리스트내 총 요소/데이터 수 반환 함수
    for index in range( len(list) ) :
        print( index ) # 0 , 1 , 2  ~
        if list[index] == findValue : # 만약에 index번째 데이터가 찾고 있는 데이터와 같으면
            pos = index # 찾았으면 찾은 위치를 pos변수에 대입
            break # 반복문 종료 # 끝 # 가장가까운 반복문 탈출 키워드
    # 반복문 종료 이후
    return pos # return 함수 종료 키워드 # return 반환값 # 반환값:함수를 호출했던 곳으로 1개의 값을 전달/반환 하는 값

# 샘플 데이터 # 사람의 키 목록
dataList = [ 188 , 162 , 150 , 168 , 155 , 182 , 177 , 172 ]
# 검색할 데이터 입력
findValue = int( input('검색할 데이터 : ') )
# 검색 함수 실행  # pos 함수(검색) 결과 # pos 검색된 데이터 인덱스위치 # -1없다 0이상 찾았다.
pos = seqSearch( dataList , findValue ) # 함수 호출/사용
if pos == -1 : # pos 가 -1 이면 못찾았다.
    print( f'{findValue} 의 검색 결과는 존재하지 않습니다.' )
else :
    print( f'{findValue} 의 검색 결과는 {pos} 위치에 존재 합니다.')

# 순차 검색 함수 정의[ + 중복허용 ]
def seqSearchDup( list , findValue ) :
    posList = [ ]

    for index in range( len(list) ) :
        if list[index] == findValue :
            posList.append( index )

    return posList


















