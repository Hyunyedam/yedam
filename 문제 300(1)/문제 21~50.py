
# 021   문자열 인덱싱
letters = 'python'
print(letters[0],letters[2])

# 022   문자열 슬라이싱
License_plate = "24가 2210"
print(License_plate[-4:]) # 뒤에서부터 4개
print(License_plate[4:8])

# 023   문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[0:6:2])

# 024   문자열 슬라이싱
string = "PYTHON"
print(string[ : : -1])

# 025   문자열 치환
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 026   문자열 다루기
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

# 027   문자열 다루기
url = "http://sharebook.kr"
url_split = url.split('-')
print(url_split[-1])

# 028   문자열은 immutable
lang = 'python'
lang[0]
print(lang) # 오류나옴

# 029   replace 메서드
string = 'abcdfe2a345a32a'
string = string.replace('a','A')
print(string)

# 030   replace 메서드
string = 'abcd'
string.replace('b','B')
print(string)

# 031   문자열 합치기
# 예상하기 => 7
a = "3"
b = "4"
print(a+b)

# 032   문자열 곱하기
# 예상하기 => HiHiHi
print("Hi" * 3)

# 033   문자열 곱하기
print("-" * 80)

# 034   문자열 곱하기
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 035   문자열 출력
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036   문자열 출력 ( 참고 )
name1 = "김민수"
age = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037   문자열 출력 ( 참고 )
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이 : {age1}")
print(f"이름: {name2} 나이 : {age2}")

# 038 이 없음...

# 039   문자열 슬라이싱 ( 참고 )
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040   strip 메서드
data = " 삼성전자 "
datal = data.strip()
print(datal)

# 041   upper 메서드
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

# 042   lower 메서드
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043   capitalize 메서드
a = "hello"
a = a.capitalize()

# 044   endswith 메서드
film_name = "보고서.xisx"
film_name.endswith("xlsx")

# 045   endswith 메서드
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))

# 046   startswith 메서드
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

# 047   split 메서드
a= "hello world"
a.split()

# 048   split 메서드
ticker = "btc_krw"
ticker.split("_")

# 049
date = "2020-05-01"
date.split("-")

# 050   retrip 메서드 ( 참고 )
data = "039490"
data = data.rstrip()