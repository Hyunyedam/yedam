#You may use import as below.
#import math

def solution(shirt_size):

    size_count = [0, 0, 0, 0, 0, 0]

    for ss in shirt_size:

        if ss == "XS":
            size_count[0] += 1
        if ss == "S":
            size_count[0] += 1
        if ss == "M":
            size_count[0] += 1
        if ss == "L":
            size_count[0] += 1
        if ss == "XL":
            size_count[0] += 1
        if ss == "XXL":
            size_count[0] += 1

    answer = []
    return answer


#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")