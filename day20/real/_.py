# 순차검색 vs 이진검색 성능차이
# 생각해보기
# 1.난수 100만개 저장되어 있는 배열
# 2. 순차검색[ 비정렬 ]이용한 검색 ( 비교 횟수 출력 )
# 3. 순차검색[ 정렬 ] 이용한 검색  ( 비교 횟수 출력 )
# 3. 이진검색[ 정렬 ] 이용한 검색  ( 비교 횟수 출력 )

# 전역변수
import random

# 순차검색 구현
def seqSearch( ary , fdata ) :
    global count
    pos = -1
    for i in range( len(ary) ) :
        count +=1
        if ary[i] == fdata :
            pos = i
            break
    return pos

# 이진검색 구현
def binSearch( ary , fdata ) :
    global count
    start = 0
    end = len(ary) -1
    while (start<=end ) :
        count += 1
        mid = ( start + end ) // 2
        if fdata == ary[mid] :
            return mid
        elif fdata > ary[mid] :
            start = mid +1
        else:
            end = mid-1
    return -1

dataAry , sortedAry = [], []
findData = 9000
count = 0

dataAry = [ random.randint( 0 , 999999) for _ in range(1000000) ]
dataAry.insert( random.randint( 0 , 1000000) , findData )
sortedAry = sorted( dataAry )

# 배열내 앞에 5개 와 뒤에 5개 출력
print("비정렬 배열 ---> " , dataAry[0:5] ,"~~~",dataAry[-5:len(dataAry)] )
print("정렬 배열 ---> " , sortedAry[0:5] ,"~~~",sortedAry[-5:len(dataAry)] )

# 성능 비교
count = 0
pos = seqSearch( dataAry , findData )
if pos != -1 :
    print('순차 검색[비정렬 데이터] --> ' , count , '회')

count = 0
pos = seqSearch( sortedAry , findData )
if pos != -1 :
    print("순차 검색[정렬 데이터] --> " , count , '회')

count = 0
pos = binSearch( sortedAry , findData )
if pos != -1:
    print("이진 검색[정렬 데이터] --> " , count , '회' )