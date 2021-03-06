

# 문제 6

def solution(number):
    count = 0 # 박수 횟수
    for i in range(1, number + 1): # 1부터 40까지 반복
        current = i # = i # 현재숫자
        temp = count # 임시변수에 박수 횟수 저장
        while current != 0: # 0이 아닐 때까지 반복
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                # 만약에 현자 숫자가 나누기 10을 했을떄 나머지가 3 혹은 6 혹은 9이면
                count += 1 # 박수 횟수 올리기
                print("pair", end='') # 박수 출력
            current = current // 10 # 현재숫자 // 10 자릿수 내리기
        if temp == count:
            print(i, end='')
        print(" ", end='')
    print(" ")
    return count

number = 40 # 1 ~ 40
ret = solution(number)

print("Solution : return value of the function is", ret, ".")