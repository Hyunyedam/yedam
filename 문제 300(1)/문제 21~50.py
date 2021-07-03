
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