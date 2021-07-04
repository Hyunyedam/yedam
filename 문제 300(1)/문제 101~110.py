
# 101   데이터 타입
print(type(True))
print(type(False))

# 102   출력 결과 예상하기
print( 3 == 5 ) # False 출력

# 103   출력 결과 예상하기
print( 3 < 5 )  # True 출력

# 104   코드 결과 예쌍하기
x = 4
print( 1 < x < 5 )

# 105   코드 결과 예상하기
print(( 3 == 3 ) and ( 4 != 3 ))

# 106   오류 발생 원인 설명하기
# print(3=>4)   # 3이 4보다 크거나 작지 않기 때문에

# 107   출력 결과 예상하기
if 4 < 3 :
    print("Hello World") # 아무것도 출력되지 않는다

# 108   출력 결과 예상하기
if 4 < 3 :
    print("Hello World")
else:
    print("Hi, there.") # Hi, there. 출력

# 109   출력 결과 예상하기  # 1 2 4 출력
if True :
    print("1")
    print("2")
else:
    print("3")
print("4")

# 110   출력 결과 예상하기  # 3 5 출력
if True :
    if False :
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")