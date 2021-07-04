
# 121
i = input("영문자를 입력해주세요 : ")
if i.islower() :
    print(i.upper())
else:
    print(i.lower())

# 122
i = int(input("score : "))
if i >= 81:
    print("grade is A")
elif i >= 60 :
    print("grade is B")
elif i >= 41 :
    print("grade is C")
elif i >= 21 :
    print("grade is D")
else:
    print("grade is E")

# 123 ( 참고 )
환율 = {"달러" : 1167, "엔":1.096, "유로":1268, "위안":171}
입력저장 = input("금액과 통화명 입력 : ")
금액 , 통화명 = 입력저장.split(" ")
print(int(금액) * 환율[통화명], "원")

# 124
i1 = int(input("input number1 : "))
i2 = int(input("input number2 : "))
i3 = int(input("input number3 : "))
if i1 > i2 and i1 > i3:
    print(i1)
elif i2 > i1 and i2 > i3:
    print(i2)
else:
    print(i3)


# 125 ( 참고 split만 )
a = input("핸드폰번호 입력 : ") # 010-3333-3333
n = a.split("-") # - 기준으로 분리 후 첫번쨰 값 가져오기 = 010
if n == "011" :
    print("당신은 SKT 입니다")
elif n == "016" :
    print("당신은 KT 입니다")
elif n == "019" :
    print("당신은 LGU 입니다")
else :
    print("알 수 없습니다.")

# 126
