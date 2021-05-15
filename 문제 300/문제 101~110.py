
# 101 : type() : 데이터의 타입[형태] 확인해주는 함수
print(type(True)) # bool : 참[True] 거짓[False] 둘 중 하나 저장하는 타입
print(type(False)) # bool : 참[True] 거짓[False] 둘 중 하나 저장하는 타입

# 102   # 예상하기
print(3 == 5)
# False 가 출력

# 103   # 예상하기
print(3 < 5)
# True 가 출력

# 104   # 예상하기
x = 4
print( 1 < x < 5)
# True 가 출력

# 105   # 예상하기
print((3 == 3) and (4 != 3))
# True 가 출력

# 106   # 에러 발생 원인 설명하기
# print(3 => 4)
# => 가 아닌 =< 를 사용해야함

# 107   # 예상하기
if 4 < 3 :
    print("Hello World")
# 아무것도 출력되지 않ㅇ음

# 108   # 예상하기
if 4 < 3:
    print("Hellow World.")
else:
    print("Hi, there.")
# Hi, there 이 출력

# 109   # 예상하기
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
# 1
# 2
# 4 출력

# 110 # 예상하기
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 3
# 5 출력