
# 141
리스트 = [100, 200, 300]
for 변수 in 리스트 : # 리스트 내 개수만큼 변수에 하나씩 대입
    print(변수 + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트 :
    print("오늘의 메뉴 : ", 변수)

# 143
리스트 = ["sk하이닉스", "삼성전자", "LG전자"]
for 변수 in 리스트 :
    print(len(변수)) # 문자열 길이가 출력

# 144
리스트 = ["dog", "cat", "parrot"]
for 변수 in 리스트 :
    print(변수, len(변수))

# 145
리스트 = ["dog", "cat", "parrot"]
for 변수 in 리스트 :
    print(변수[0]) # 0번째 인덱싱 = 첫글자

# 146
리스트 = [1, 2, 3]
for 변수 in 리스트 :
    print("3 x", 변수)
        # 일반문자는 " " 사용 0        # 변수는 " " 사용 x

# 147
리스트 = [ 1, 2, 3]
for 변수 in 리스트 :
    print("3 x", 변수, "=", (3*변수))

# 148
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[1: ] :
    print(변수)

# 149
리스트 = ["가","나","다","라"]
for 변수 in 리스트 [ 0 : 3 : 2 ]: # 0번부터 3번까지 2씩 증가
    print(변수)

# 150
리스트 = ["가","나","다","라"]
for 변수 in 리스트[ : : -1] : # 0번부터 끝까지 -1 역순으로 증가
    print(변수)