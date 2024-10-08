# [4] 퀵 정렬
dataList = [ 188 , 162 , 168 , 155 ,  158 , 177 , 172 ]
# 퀵 정렬 함수 구현
def quickSort( list ) :
    n = len( list ) # 리스트내 요소(데이터) 총 개수
    if n <= 1 :  # 만약에 길이가 1 이하 이면 함수 종료
        return list
    # 리스트내 가운데 인덱스를 피벗(기준)으로 선정
    pivot = list[ n//2 ]
        # 길이가 홀수이면  7 // 2 -> 3.5 -> 3  (가운데)    # 길이가 짝수이면  8 // 2 -> 4
    left = [ ] # 기준(피벗) 보다 작은 데이터들 저장
    right = [ ] # 기준(피벗) 보다 큰 데이터들 저장
    # 리스트내 요소 하나씩 반복
    for i in list :
        if i < pivot : # i값이 피벗(기준보다) 작으면 왼쪽리스트
            left.append( i )
        elif i > pivot : # i값이 더 크면 오른쪽리스트
            right.append( i )
    # for end
    return quickSort( left ) + [ pivot ] + quickSort( right ) # 재귀함수

print( dataList ) # 정렬 전 # [188, 162, 168, 155, 158, 177, 172]
print( quickSort( dataList ) ) # 정렬 후 # [155, 158, 162, 168, 172, 177, 188]


# [5] 퀵 정렬 ( + 중복 허용 )
# 퀵 정렬 함수 구현
def quickSort2( list ) :
    n = len( list ) # 리스트내 요소(데이터) 총 개수
    if n <= 1 :  # 만약에 길이가 1 이하 이면 함수 종료
        return list
    # 리스트내 가운데 인덱스를 피벗(기준)으로 선정
    pivot = list[ n//2 ]
        # 길이가 홀수이면  7 // 2 -> 3.5 -> 3  (가운데)    # 길이가 짝수이면  8 // 2 -> 4
    left = [ ] # 기준(피벗) 보다 작은 데이터들 저장
    right = [ ] # 기준(피벗) 보다 큰 데이터들 저장
    middle = [ ] # 기준(피벗) 값과 같은 데이터들 저장
    # 리스트내 요소 하나씩 반복
    for i in list :
        if i < pivot : # i값이 피벗(기준보다) 작으면 왼쪽리스트
            left.append( i )
        elif i > pivot : # i값이 더 크면 오른쪽리스트
            right.append( i )
        else:  # i값과 피벗값이 같으면
            middle.append(i)
    # for end
    return quickSort( left ) + middle  + quickSort( right ) # 재귀함수


















