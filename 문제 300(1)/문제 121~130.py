
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
a = input("핸드폰번호를 입력해주세요 ( - 포함 ) : ")
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
a = input("우편번호 : ")
a = a[0 : 3]
if a in [ "010", "011", "012"]: # 강북구 번호가 포함이 되어 있으면
    print("강북구")
elif a in ["014", "015", "016"]: # 도봉구 번호가 포함되어 있으면
    print("도봉구")
else : # 그외 [나머지]
    print("노원구")

# 127 [참고]
i = input("주민등록번호 : ")
i= i.split("-")[1]
if i[0] == "1" or i[0] == "3" :
    print("남자")
else :
    print("여자")

# 128
i = input("주민등록번호 : ")
n = i.split("-")[1]
if 0 <= int(n[1: 3]) <= 8:
    print("서울 입니다")
else:
    print("부산 입니다")

# 129 [참고]
a=input("주민등록번호:")
f = int(a[0])*2 + int(a[1])*3+ int(a[2])*4 + int(a[3])*5 + int(a[4])*6+ int(a[5])*7 + int(a[7])*8+ int(a[8])*9+ int(a[9])*2+ int(a[10])*3 + int(a[11])*4 + int(a[12])*4
        #주민번호[6]: - 제외
s = 11-(f%11)
t = str(s) #문자로 변환
if a[-1] == t[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

 # 130 [ 참고 ]
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = int(btc["max_price"]) - int(btc["min_price"])
시가 = int(btc["opening_price"])
최고가 = int(btc["max_price"])

if 시가 + 변동폭 > 최고가:
    print("상승장")
else:
    print("하락장")