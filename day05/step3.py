# 1. continue 키워드 : 현재 반복을 중단 하고 다음 반복으로 넘어갈때
# 1. 1부터 10까지의 숫자 중에 홀수만 출력하기.
for value in range(1, 11):  # 1부터 10까지 1씩증가 반복 처리
    if value % 2 == 0:  # 만약에 반복변수가 짝수이면
        continue  # continue 을 만나면 반복을 중단하고 다음 반복으로 넘어갑니다.
    print(value)  # 짝수일때는 print() 안된다.

    # 2. 1부터 10까지의 숫자 중 3 , 5를 제외한 출력하기
for value in range(1, 11):
    if value == 3 or value == 5:
        continue
    print(value)

# 2. break 키워드 : 현재 반복을 중단 하고 더 이상 반복문을 실행하지 않는다.[ 반복문 종료, 반복문 바깥쪽으로 이동 ]
# 1. 1부터 10까지의 숫자 중에 5이상 되면 반복문 종료
for value in range(1, 11):
    print(value)
    if value >= 5: break

    # 2. 1부터 10까지의 숫자 중 7이면 반복문 종료
for value in range(1, 11):
    print(value)  # 1 2 3 4 5 6 7
    if value == 7: break
    # print(value)          # 1 2 3 4 5 6

# [실습1] 1부터 100까지 누적합계를 구하는데 누적합계가 1000초과 하면 중지 하고 누적합계 출력 하시오.
sum = 0  # 누적합계의 값을 저장 할 변수 선언
for value in range(1, 101):
    sum += value
    if sum > 1000:
        break  # 만약에 누적합계가 1000 초과하면 반복문 종료
    # if sum > 1000 :
    #     continue        # 만약에 누적합계가 1000 초과하면 반복 중단하고 다음 반복으로 이동 ,
    # sum += value        # 누적합계가 1000 초과이면 실행이 안되는 코드.....

print(sum)

# [실습2] 반복 횟수를 입력 받아 입력 받은 횟수 만큼 반복 입력 받고 출력하시오. 만약에 x 입력하면 반복문 종료
# ex) 반복횟수가 10를 입력했으면 10번 입력받기 , 단 x 입력시 반복 종료
입력횟수 = int(input('[실습2] 입력받을 횟수 : '))
for count in range(입력횟수):
    메시지 = input(' [실습2] (x:종료) 메시지 입력 : ')
    if 메시지 == 'x' or 메시지 == 'X':
        break

# 반복문이 어려운점 : 코드에서 눈으로 볼수 없는 흐름 존재..
# 눈에 안보이는것을 작성해보세요.
for value in range(10):
    print(value)
    if value == 7:
        break
    # 1. 코드 의 순서도를 작성한다.
    '''
                            if value == 7       break 만나기 
        value = 0 일때            False       
        value = 1 일때            False       
        value = 2 일때            False   
        value = 3 일대            False 
        value = 4 일때            False
        value = 5 일때            False
        value = 6 일때            False
        value = 7 일때            True            break       ---> for문 종료 

    '''

# 2. 반복문 안에 있는 모든 변수들을 print() 출력해서 console창에서 육안으로 확인



