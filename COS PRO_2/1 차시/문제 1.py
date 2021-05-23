

# 문제 1 : 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기

def solution(shirt_size):   # 함수 만들기

    size_count = [0, 0, 0, 0, 0, 0] # 리스트 선언 ( 사이즈 갯수 만큼 )
                 # XS, S, M, L, XL, XXL
    for ss in shirt_size : # 리스트 반복 => 리스트내 항목이 변수에 하나씩 대입
        if ss == "XS":                  # 만약에 XS 이면 첫번째 인덱스 +1
            size_count[0] += 1
        if ss == "S":                   # 만약에 S 이면 첫번째 인덱스 +1
            size_count[1] += 1
        if ss == "M":                   # 만약에 M 이면 첫번째 인덱스 +1
            size_count[2] += 1
        if ss == "L":                   # 만약에 L 이면 첫번째 인덱스 +1
            size_count[3] += 1
        if ss == "XL":                  # 만약에 XL 이면 첫번째 인덱스 +1
            size_count[4] += 1
        if ss == "XXL":                 # 만약에 XXL 이면 첫번째 인덱스 +1
            size_count[5] += 1
    return size_count                   # 티셔츠를 사이즈별로 리스트 반환

    # 함수가 끝나면서 돌려주는 값 => return => 리스트를 리턴
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size) # 함수 불러내기

print("solution : return value of the funcion is", ret, ".")