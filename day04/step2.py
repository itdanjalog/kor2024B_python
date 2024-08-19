
# 문제 9개 풀이 : http://itdanja.cafe24.com/study/info/view?cno=21&bno=372
    # 반복문 사용 불가능 , 입출력,변수,연산자,조건문 을 활용합니다.
	# 모두 풀이 했으면 메일(itdanja@kakao.com) 로 제출

#문제1 : 점수를 정수형으로 입력받아 점수가 90점 이상이면 '합격' 아니면 '불합격' 출력 하시오.
#[풀이]
value1 = int( input('[문제1]점수 : ') ) # 1. 입력받고 -> 정수형변환 -> 변수에 저장
if value1 >= 90 :		# 주의할점 : if 조건식 :(콜론) 잊미말고 작성 해주세요.
	print('합격')		# 주의할점 : print()앞에 tab키 이용한 들여쓰기 꼭 해주세요.
else :
	print('불합격')
#문제2 : 점수를 정수형으로 입력받아 점수가 90점 이상이면 'A등급', 80점 이상이면 'B등급', 70점 이상이면 'C등급', 그외 '재시험' 으로 출력 하시오.
value2 = int( input('[문제2]점수 : '))
if value2 >= 90 : print('A등급')
elif value2 >= 80 : print('B등급')
elif value2 >= 70 : print('C등급')
else : print('재시험')

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

if value4_1 > value4_2 : value4_1 , value4_2 = value4_2 , value4_1
if value4_1 > value4_3 : value4_1 , value4_3 = value4_3 , value4_1
if value4_2 > value4_3 : value4_2 , value4_3 = value4_3 , value4_2

print( value4_1 , value4_2 , value4_3 )


