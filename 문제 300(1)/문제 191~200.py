
# 191 [ 참고 ]
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for column in line:
        print(column * 1.00014)

# for : 반복문
# for 변수 in 리스트 :   # 리스트내 요소 하나씩 변수에 대입 반복
# for 중첩
    # for 변수1 in 2차원리스트 :   # 2차원리스트내 리스트 하나씩 변수1 대입 반복
        # for 변수2 in 변수1 :      #1차원리스트내 요소 하나씩 변수에 대입

# 192 [ 참고 ]
for line in data:
    for column in line:
        print(column * 1.00014)
    print("----")

# 193 [ 참고 ]
result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)

# 194 [ 참고 ]
result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])

# 196
for row in ohlc[1:]:
    if row[3] > 150 :
        print(row[3])

# 197
for row in ohlc[1:]:
    if (row[3] > row[0]):
        print(row[3])

# 198
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])

# 199
for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[1]-row[2])

# 200
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
