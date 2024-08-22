# 조건문 실습1
    # 하나의 점수를 입력 받아 점수 변수에 저장 하기.
    # 점수 변수가 80점 이상 이면 '합격' 아니면 '불합격' 출력 하시오.
# 1. 하나의 점수를 입력받기  , input('점수 : ')
# 2. 정수 타입 으로 변환 ,  int( input('점수 : ') )
# 3. 논리 하기 위해 변수 기억/저장/대입 , point = int( input('점수 : ') )
point = int( input('점수 : ') )
# 4. 논리/판단
    # 조건문 : 점수 변수가 80점 이상  , point >= 80
    # 참 : '합격' 출력  , print( '합격' )
    # 거짓 : '불합격' 출력 , print( '불합격')
'''
if 조건문 : 
    참
else :
    거짓
'''
if point >= 80 :
    # 들여쓰기
    print( '합격' )
else:
    print( '불합격' )

# 조건문 실습2
    # 하나의 점수를 입력 받아 점수 변수에 저장 하기
    # 점수 변수가 90점 이상 이면 'A등급'
    #            80점 이상 이면 'B등급'
    #            70점 이상 이면 'C등급'
    #            그외 '재시험' 출력 하시오.
score = int( input('점수 : ') )
# 조건1: 점수 변수가 90점 이상 , score >= 90 #참1: 'A등급' 출력 , print('A등급')
# 조건2: 점수 변수가 80점 이상 , score >= 80 #참2: 'B등급' 출력 , print('B등급')
# 조건3: 점수 변수가 70점 이상 , score >= 70 #참3: 'C등급' 출력 , print('C등급')
# 그외 : #거짓 '재시험' 출력 , print('재시험')
'''
if 조건1 : 
    참1
elif 조건2 : 
    참2
elif 조건3 : 
    참3 
else : 
    거짓
'''
if score >= 90 :
    print('A등급')
elif score >= 80 :
    print('B등급')
elif score >= 70 :
    print('C등급')
else :
    print('재시험')
#  if ~ elif ( 다중 조건의 결과는 1개 ) vs 다중 if( 다중 조건의 결과 N개 )
if score >= 90 :
    print('A등급')
if score >= 80 :
    print('B등급')
if score >= 70 :
    print('C등급')
else :
    print('재시험')
