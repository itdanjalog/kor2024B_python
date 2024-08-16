# day02 > step3.py

# [1] 출력 함수 , print( 리터럴값 또는 변수명 ) ,
    # print( ) 소괄호 안에 있는 값이 콘솔 창에 출력 하는 함수
print( 10 ) # 10 출력
실수상자 = 3.14
print( 실수상자 ) # 변수안 에 있는 데이터 를 호출 한 뒤 출력 된다.

# [2] 문자열 연결
    # 1. ,(쉼표)를 이용한 여러개 문자열을 출력하기 , 사이에 공백이 추가 됩니다.
print( "파이썬" , "문법" , "학습중" )
    # 2. +(더하기)를 이용한 여러개 문자열을 출력하기
print( "파이썬" + "문법" + "학습중" )

# [3] 문자열 과 연산코드를 연결 하여 문자열 만들기 , f 포메팅 , py v3 이상 부터 ~
print( f"파이썬 문법 학습중 ") # f"문자열" , 문자열이 구성됨.
print( f"파이썬 문법 학습중 { 실수상자 } ") # f"문자열{ }문자열" ,
# { } 중괄호 를 이용한 문자열 사이에 변수값이나 리터럴값을 연결할수 있다.
# 응용1
name = "유재석" # 'name' 변수에 "유재석" 이라는 문자열 리터럴 값 대입
age = 42    # 'age' 변수에 42 이라는 정수 리터럴 값 대입
print( f"나의 이름은 { name } 이고 나이는 { age + 10 } 살 입니다. ")
    # 실행순서
    # 1) print( f"나의 이름은 유재석 이고 나이는 { age + 10 } 살 입니다. ")
    # 2) print( f"나의 이름은 유재석 이고 나이는 { 42 + 10 } 살 입니다. ")
    # 3) print( f"나의 이름은 유재석 이고 나이는 52 살 입니다. ")
    # 4) 나의 이름은 유재석 이고 나이는 52 살 입니다.
# (3-2) 자릿수 맞추기
print( f"나이 : {age:<5}")        # {값:<자릿수} : 값을 자릿수 만큼 차지,왼쪽 정렬
 # {age:<5} 안에서 띄어쓰기 금지.
print( f"나이 : {age:>5}")        # {값:>자릿수} : 값을 자릿수 만큼 차지,오른쪽 정렬
print( f"나이 : {age:^5}")        # {값:^자릿수} : 값을 자릿수 만큼 차지,가운데 정렬
    # ^특수문자 : shift + 6
# (3-3) 소수점 자릿수 맞추기
print( f"키 :{165.15:0.1f}")    # {값:[총자릿수].[소수자릿수]f} , 잘린 소수점은 반올림이 된다.
pi = 3.141592
print( f"pi :{ pi:>10.3f}")     # {pi:>10.3f} , 총 10칸 이고 오른쪽 정렬 하면서 소수점은 3칸 , 잘린 부분에서 반올림 이된다.

# [4] 이스케이프/제어 문자 , 제어기능이 담긴 문자들 , 컴퓨터 규칙 , 다른언어들과 공통
    # 1. \n : 문자열의 줄을 바꿔 주는 기능이 담긴 문자
    # 2. \t : 문자열의 들여쓰기[tab]를 해주는 기능이 담긴 문자
    # 3. \\ : 문자열의 '\' 백슬래시를 출력해주는 기능 담긴 문자
        # \백슬래시 : 키보드 엔터 위에 '원화기호' 기호
        #  주의할점 : \ 한개 이면 이스케이프 기능 이므로 백슬래시 출력시 에는 \\ 백슬래시 두번하면 한번이 출력된다.
    # 4. \" : 문자열의 " 큰따옴표를 출력해주는 기능 담긴 문자
    # 5. \' : 문자열의 ' 작은따옴표를 출력해주는 기능이 담긴 문자
        # " 또는 ' 는 한개 가 있으면 문자열타입 기능 이므로 " 또는 ' 출력시 에는 \' 백슬래시 함께 작성한다.
print("안녕 파이썬") # 안녕 파이썬
print("안녕\n파이썬")
# 안녕
# 파이썬
print("A\tB")   # A  B  , 한칸 vs 탭[들여쓰기] 서로 다르다.
# print("안녕"파이썬"") # 오류발생 : 문자열타입를 구분하는 " 와 출력하는 " 와 구분이 불가능.
print("안녕\"파이썬\"") # 안녕"파이썬"
print('안녕"파이썬"')  # 안녕"파이썬"
print("안녕'파이썬'")  # 안녕'파이썬'
print("안녕\'파이썬\'") # 안녕'파이썬'





