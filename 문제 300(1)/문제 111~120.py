
# 111   문자열 출력하기
a = '안녕하세요'
print(a*2)

# 112   숫자 입력받아 출력하기
a = int(input("숫자를 입력하세요 : "))
print(a + 10)

# 113   짝수 홀수 판별하기
a = int(input("짝수/홀수 판별할 숫자를 입력하세요 : "))
if a/2 == 0:
    print("짝수")
else:
    print("홀수")

# 114   숫자 입력받아 출력하기
a = int(input('입력값 : '))
if a > 255:
    print(255)
else :
    print(a + 20)

# 115
a = int(input("20을 뺄 값을 입력하세요 : "))
if a-20 > 255 :
    print(255)
elif a-20 < 0 :
    print(0)
else:
    print(a-20)

# 116
i = input("시간을 입력하세요 : ")
if i[-2: ] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")

# 117
fruit = ["사과", "포도", "홍시"]
a = input("좋아하는 과일은? : ")
if a in fruit:
    print("정답입니다")
else:
    print("오답입니다")

# 118
warn_inverstment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a = input("종목명을 입력해주세요 : ")
if a in warn_inverstment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

# 119
fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
i = input("제가 좋아하는 계절은? : ")
if i in fruit :
    print("정답입니다")
else:
    print("오답입니다")

# 120
fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
i = input("좋아하는 과일은? : ")
if i in fruit.values() :
    print("정답입니다")
else :
    print("오답입니다")