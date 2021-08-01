

# 171
가격목록 = [32100,32150,32000,32500]

for 변수 in 가격목록 :
    print(변수)

for i in range(4) :
    print(가격목록)

# 172
가격목록 = [32100,32150,32000,32500]
for i, 변수 in enumerate(가격목록) :
    print(i, 변수)

# 173
가격목록 = [32100,32150,32000,32500]
for i in range(len(가격목록)):
    print(3-i, 가격목록[i])

# 174
for i in range(1, 4):
    print(90 + 10 * i, 가격목록[i])

# 175
my_list = ["가","나","다"]

print(my_list[0], my_list[1])
print(my_list[1], my_list[2])
print(my_list[2], my_list[3])

for i in [0, 1, 2]:
    print(my_list[i])

for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1])

for i in range( len(my_list) - 1 ) :
  print(my_list[i], my_list[i+1])

for i in range( 1, len(my_list) ) :
  print(my_list[i-1], my_list[i])

# 176
my_list = ["가","나","다"]

print(my_list[0], my_list[1], my_list[2])
print(my_list[1], my_list[2], my_list[3])
print(my_list[2], my_list[3], my_list[4])

for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1], my_list[i+2])

# 178
for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    f = (my_list[i]+ my_list[i+1] + my_list[i +2]) /3
    print(f)

# 180
low = [100, 200 , 400, 800, 1000]
high = [150, 300, 430, 880, 1000]
v = []
for i in range (0,5):
    v.append(low[i]-high[i])

