
# 121
입력저장 = input("영문입력 : ")
if 입력저장.islower() : # 소문자이면 True 아니면 false
    print(입력저장.upper()) # 대문자로 변환
else :
    print(입력저장.lower()) # 소문자로 변환

# 122
점수 = int(input("점수입력"))
if 점수 >= 81 :
    print("A 등급")
elif 점수 >= 61 :
    print("B 등급")
elif 점수 >= 41 :
    print("C 등급")
elif 점수 >= 21 :
    print("D 등급")
else:
    print("E 등급")

# 123
환율 = {"달러" : 1167, "엔":1.096, "유로":1268, "위안":171}
입력저장 = input("금액과 통화명 입력 : ")
금액 , 통화명 = 입력저장.split(" ") # 공백 기준으로 분리
print(int(금액) * 환율[통화명], "원") # 환율 딕셔너리에서 입력한 통화명 찾아서 값 가져오기

# 124
숫자1 = int(input("숫자1 입력 : "))
숫자2 = int(input("숫자2 입력 : "))
숫자3 = int(input("숫자3 입력 : "))

# 정답 1
print(max(숫자1, 숫자2, 숫자3))
# 정답 2
if 숫자1 > 숫자2 and 숫자1 > 숫자3 : # 숫자1이 숫자 2보다 크면서 숫자3 보다 크면
    print(숫자1)
elif 숫자2 > 숫자1 and 숫자2 > 숫자3 : # 숫자2가 숫자1보다 크면서 숫자3보다 크면
    print(숫자2)
else :
    print(숫자3)

# 125
핸드폰번호 = input("핸드폰번호 입력 : ") # 010-3333-3333
통신사번호 = 핸드폰번호.split("-") # - 기준으로 분리 후 첫번쨰 값 가져오기 = 010
if 통신사번호 == "011" :
    print("당신은 SKT 입니다")
elif 통신사번호 == "016" :
    print("당신은 KT 입니다")
elif 통신사번호 == "019" :
    print("당신은 LGU 입니다")
else :
    print("알 수 없습니다.")

# 126
우편번호 = input("우편번호 : ")
우편번호 = 우편번호[0 : 3] # 0 ~ 2 까지 가져오기 [ 앞 3자리 ]
if 우편번호 in [ "010", "011", "012"]: # 강북구 번호가 포함이 되어 있으면
    print("강북구")
elif 우편번호 in ["014", "015", "016"]: # 도봉구 번호가 포함되어 있으면
    print("도봉구")
else : # 그외 [나머지]
    print("노원구")

# 127
주민번호 = input("주민등록번호 : ")
주민번호 = 주민번호.split("-")[1] # -기준으로 분리 했을때 두번째 값 가져오기
if 주민번호[0] == "1" or 주민번호[0] == "3" :
    print("남자")
else :
    print("여자")

# 128
주민번호 = input("주민등록번호 : ")
뒷자리 = 주민번호.split("-")[1] # - 기준으로 분리 했을때 뒷자리 가져오기
# 00 ~ -8 : 서울 // 09~ 12 부산
if 0 <= int(뒷자리[1: 3]) <= 8 :
    print("서울 입니다")
else:
    print("부산 입니다")

# 129
a=input("주민등록번호:")
f = int(a[0])*2 + int(a[1])*3+ int(a[2])*4 + int(a[3])*5 + int(a[4])*6+ int(a[5])*7 + int(a[7])*8+ int(a[8])*9+ int(a[9])*2+ int(a[10])*3 + int(a[11])*4 + int(a[12])*4
        #주민번호[6]: - 제외
s = 11-(f%11)
t = str(s) #문자로 변환
if a[-1] == t[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
    #해당 주소의 딕셔너리 가져오기[data] 키의 값을 가져오기
변동폭 = int(btc["max_price"])-int(btc["min_price"]) #최고가-최저가 => 차이
시가 = int(btc["opening_price"]) #시가 가격
최고가 = int(btc["max_price"])

if 시가 +변동폭>최고가:
    print("상승장")
else:
    print("하락장")