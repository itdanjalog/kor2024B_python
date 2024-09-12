# [문제1] 문자열 길이 반환
# [ 지문 ]  하나의 문자열을 입력받아 그 문자열의 길이를 반환하는 string_length 함수를 정의하세요.
# [ 요구사항 ]
# 1. string_length 함수는 하나의 문자열을 매개변수로 받아야 합니다.
# 2. 문자열의 길이를 반환하세요.
# 3. 함수 호출 예시: string_length("hello")는 5를 반환해야 합니다.
def string_length(a) :
    r = len(a)
    return r

result = string_length('hello')
print(result)


# [문제2] 최대값 찾기
# [ 지문 ]  정수로 이루어진 리스트를 입력받아 그 리스트에서 최대값을 반환하는 find_max 함수를 정의하세요.
# [ 요구사항 ]
# 1. find_max 함수는 정수 리스트를 매개변수로 받아야 합니다.
# 2. 리스트에서 가장 큰 값을 반환하세요.
# 3. 리스트가 비어있으면 0을 반환하세요.
# 4. 함수 호출 예시: find_max([1, 3, 2, 5, 4])는 5를 반환해야 합니다.
def find_max(a) :
    if len(a) > 0 :
        result1 = max(a[:])
        return result1
    else :
        result2 = 0
        return result2

print(find_max([1,2,3,4,5]))


# [문제3] 두 숫자의 차이
# [ 지문 ]  두 개의 정수를 입력받아 그 차이를 반환하는 subtract_numbers 함수를 정의하세요.
# [ 요구사항 ]
# 1. subtract_numbers 함수는 두 개의 정수 매개변수를 받아야 합니다.
# 2. 두 정수의 차이를 반환하세요 (첫 번째 정수에서 두 번째 정수를 뺍니다).
# 3. 함수 호출 예시: subtract_numbers(10, 4)는 6을 반환해야 합니다.

def subtract_numbers(a, b) :
    result = a - b
    return result

abc = subtract_numbers(10, 4)
print(abc)


# [문제4] 문자열 역순
# [ 지문 ] 하나의 문자열을 입력받아 그 문자열을 역순으로 변환하여 반환하는 reverse_string 함수를 정의하세요.
# [ 요구사항 ]
# 1. reverse_string 함수는 하나의 문자열을 매개변수로 받아야 합니다.
# 2. 문자열을 역순으로 변환하여 반환하세요.
# 3. 함수 호출 예시: reverse_string("hello")는 "olleh"를 반환해야 합니다.

def reverse_string(a) :
    result = a.reversed()
    return result

cba = reverse_string('hello')
print(cba)

a = 'hello'
print(a.reverse())

# AttributeError: 'str' object has no attribute 'reverse'라는 오류 발생



# [문제5] 숫자 제곱
# [ 지문 ]
# [ 요구사항 ]
# 1. square_number 함수는 하나의 숫자 매개변수를 받아야 합니다.
# 2. 입력받은 숫자의 제곱을 반환하세요.
# 3. 함수 호출 예시: square_number(4)는 16을 반환해야 합니다.
def square_number(a) :
    result = a ** 2
    return result

print(square_number(4))