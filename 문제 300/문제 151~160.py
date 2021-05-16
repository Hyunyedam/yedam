
# 151
리스트 = [3, -20, -3, 44]
for 변수 in 리스트 :
    if 변수 < 0 : # 만약에 변수가 0보다 작으면
        print(변수) # 출력
    # 아니면 생략

# 152
리스트 = [3, 100, 23, 44]
for 변수 in 리스트 :
    if 변수 % 3 == 0 : # 만약에 변수가 % 3 을 했을 때 나머지가 0이면
        print(변수)
    # 아니면 출력

# 153
리스트 = [13,21,12,14,30,18]
for 변수 in 리스트 :
    if 변수 < 20 and 변수 % 3 == 0 :
        print(변수)

# 154
리스트 = ["I", "study", "python", "Language", "!"]
for 변수 in 리스트 :
    if len(변수) >= 3 : # 만약에 글자수가 3글자 이상이면
        print(변수)

# 155
리스트 = ["A", "B", "C", "D"]
for 변수 in 리스트 :
    if 변수.isupper(): # 만약에 변수가 대문자이면
        print(변수)

# 156
리스트 = ["A", "B", "C", "D"]
for 변수 in 리스트 :
    if 변수.isupper() :
        print(변수)

# 157
리스트 = ["dog", "cat", "parrot"]
for 변수 in 리스트 :
    print(변수.isupper())

# 158
리스트 = ["hello.py", "ex01.py", "intro.hup"]
for 변수 in 리스트 :
    분리 = 변수.split(".") # . 기준으로 분리
    print(분리[0]) # 분리 기준으로 앞문자 출력

# 159
리스트 = ["intra.h", "intra.c", "define.h", "run.py"]
for 변수 in 리스트 :
    분리 = 변수.split(".") # . 기준으로 분리
    if 분리[1] == "h": # 분리 기준으로 2번째 문자 비교
        print(변수)

# 160
리스트 = ["intra.h", "intra.c", "define.h", "run.py"]
for 변수 in 리스트 :
    분리 = 변수.split(".") # . 기준으로 분리
    if 분리[1] == "h" or 분리[1] == "c" : # 분리 기준으로 2번째 문자 비교
        print(변수)