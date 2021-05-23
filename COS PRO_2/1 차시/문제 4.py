

# 문제 4

def func_a(arr): # 1단계 함수 : 각 자연수들의 개수 세기
    counter = [0 for _ in range(1001)]
        # 자연수들 마다 개수를 저장하는 리스트
    for x in arr: # 리스트 반복
        counter[x] += 1 # 각 자연수 위치 인덱스에 +1
    return counter

def func_b(arr): # 2단계 함수 : 가장 ㅁ낳이 등장하는 수 세기
    ret = 0 # 가장 많은 개수를 가지고 있는 자연수를 찾아서 저장하는 변수
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr): # 3단계 함수 : 가장 적게 등장하는 수 세기
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt # 4단계 비율 구하기

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2] # 자연수가 있는 리스트
ret = solution(arr)

print("Solution : return value of the funcion is", ret, ".")