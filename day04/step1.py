
# [예제1]
c = 'sweet'
# [삼항연산자 방법1]
print( '삼키다' if c == 'sweet' else '뱉는다')
# [조건문 방법2]
if c == 'sweet' : print('삼키다')
else :  print('뱉는다')
# [예제2]
if 3 > 1 : print('3이 크다.')
# [예제3]
if 3 > 5 : print('3이 5보다 크다.')
else : print('3이 5보다 작다')
# [예제4]
if 3 > 5 : print('3이 5보다 크다')
elif 3 > 4 : print('3이 4보다 크다')
elif 3 > 3 : print( '3이 3보다 크다')
elif 3 > 2 : print( '3이 2보다 크다')
else : print('[참이 없다.]')

#[ 실습1 ] 하나의 점수를 입력받아 80점 이상이면
#           '합격' 아니면 '불합격' 출력하시오.
#[풀이]
point = int( input('[실습1] 점수 : ') )
if point >= 80 : print('합격')
else : print('불합격')

#[ 실습2 ] 하나의 점수를 입력받아 90점이상 "A등급" 80점 이상 "B등급"
            # 70점 이상이면 "C등급" 그외 탈락 출력하시오.
point2 = int( input('[실습2] 점수 : ') )
if point2 >= 90  : print('A등급')
elif point2 >= 80 : print("B등급")
elif point2 >= 70 : print("C등급")
else : print('탈락')
# vs
if point2 >= 90  :
    print('A등급')
elif point2 >= 80 :
    print("B등급")
elif point2 >= 70 :
    print("C등급")
else :
    print('탈락')




