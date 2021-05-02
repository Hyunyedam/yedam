
# 문제 21 : 인덱싱 [문자순서] : 0번 시작
letters = 'python'
print(letters[0],letters[2])

# 문제 22 : 슬라이싱 [ 시작번호, 끝번호, 단위 ]
    # 시작번호부터 끝번호 전까지의 문자 출력
License_plate = "24가 2210"
print(License_plate[-4:]) # 뒤에서부터 4개
print(License_plate[4:8])

# 문제 23
string = "홀짝홀짝홀짝"
print(string[0:6:2]) # 0부터 6전까지 2단위로 이동

# 문제 24 : 슬라이싱 반대로
string = "PYTHON"
print(string[ : : -1]) # 뒤에서부터 시작

# 문제 25 : replace ( "기존문자" , "새로운문자" ) 교체 함수
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 문제 26
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

# 문제 27
url = "http://sharebook.kr"
url_split = url.split('-')
print(url_split[-1])

# 문제 28
    # 오류 발생
lang = 'python'
lang[0]
print(lang)

# 문제 29
string = 'abcdfe2a345a32a'
string = string.replace('a','A')
print(string)

# 문제 30
    # abcd 가 그대로 출력됨
string = 'abcd'
string.replace('b','B')
print(string)

