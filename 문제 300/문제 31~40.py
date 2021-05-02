
# 문제 31
    # 34가 출력된다
a = "3"
b = "4"
print(a+b)

# 문제 32
    # Hi 가 연속으로 3번 반복된다
print("Hi" * 3)

# 문제 33
print("-" * 80)

# 문제 34
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 문제 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 문제 36
name1 = "김민수"
age = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 문제 37
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이 : {age1}")
print(f"이름: {name2} 나이 : {age2}")

# 문제 38
상장주식수 = "5, 969, 782, 550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

# 문제 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 문제 40
data = " 삼성전자 "
datal = data.strip()
print(datal)