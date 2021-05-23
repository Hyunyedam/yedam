
# 문제 5

def solution(arr):
    left, right = 0, len(arr)-1
    while left < right: # 오른쪽이 더 클 경우에만
        arr[left], arr[right] = arr[right], arr[left]
            # 첫번째값[왼], 첫번
        left += 1 # 왼쪽 1증가
        right -= 1 # 오른쪽 1감소
    return arr

arr = [1, 4 , 2, 3]
ret = solution(arr)

print("Solution : return value of the function is", ret, ".")