
# 211 함수 호출 결과 예측
def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")
# 예측 결과 : 안녕, Hi

# 212
def 함수(a,b) :
    print(a+b)

함수(3,4)
함수(7,8)
# 예측 결과 : 7, 15

# 213 에러 발생 원인 설명
# def 함수(문자열):
#     print(문자열)
# 함수()
# 에러 발생 원인 : 문자열이나 함수 안에 변수가 들어있지 않기 때문

# 214 에러 발생 원인 설명
# def 함수 (a,b):
#     print(a+b)
#
# 함수("안녕", 3)
# 에러 발생 원인 : 변수가 문자가 아닌 수가 들어가야 하기 때문

# 215
def print_with_smile(string):
    print(string + ":D")

# 216
print_with_smile("안녕하세요")

# 217
def print_upper_price(price) :
    print(price * 1.3)

# 218
def print_sum():
    i = int(input("첫번째 숫자를 입력하세요 : "))
    a = int(input("두번째 숫자를 입력하세요 : "))
    print(i+a)
print_sum()

# 219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

# 220
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

