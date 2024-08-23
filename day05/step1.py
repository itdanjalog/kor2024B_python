#문제3 : 각 3개의 정수형으로 수를 입력받아 가장 큰 수를 출력 하시오. [ 전제조건 : 각 정수는 서로 다른 정수값 ]
#[풀이]
# 정수 3개를 입력받아 각 변수에 저장
value3_1 = int( input('[문제3] 정수1:'))
value3_2 = int( input('[문제3] 정수2:'))
value3_3 = int( input('[문제3] 정수3:'))
# 가장 큰수를 저장하는 변수 선언하고 가장큰수를 저장하는 변수에 첫번째 값 저장
max = value3_1
# 가장 큰수와 두번째 입력값과 비교후 입력값이 더 크면 입력값을 가장 큰수 변수에 저장
if max < value3_2 :
	max = value3_2
# 가장 큰수와 세번째 입력값과 비교후 입력값이 더 크면 입력값을 가장큰수 변수에 저장
if max < value3_3 :
	max = value3_3
# 가장 큰수 변수 출력
print('가장 큰수 : ' , max )


#[풀이2]
if value3_1 > value3_2 and value3_1 > value3_3 : print( value3_1 )
elif value3_2 > value3_1 and value3_2 > value3_3 : print( value3_2 )
else : print( value3_3 )

#문제4 : 각 3개의 정수형으로 수를 입력받아 오름차순 순서대로 출력하시오. [ 전제조건 : 각 정수는 서로 다른 정수값 ]
value4_1 = int( input('[문제4] 정수1:'))
value4_2 = int( input('[문제4] 정수2:'))
value4_3 = int( input('[문제4] 정수3:'))

if value4_1 > value4_2 :
    value4_1 , value4_2 = value4_2 , value4_1
if value4_1 > value4_3 :
    value4_1 , value4_3 = value4_3 , value4_1
if value4_2 > value4_3 :
    value4_2 , value4_3 = value4_3 , value4_2

print( value4_1 , value4_2 , value4_3 )
