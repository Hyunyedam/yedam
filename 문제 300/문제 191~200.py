
# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for column in line:
        print(column * 1.00014)

# 192
for line in data:
    for column in line:
        print(column * 1.00014)
    print("----")

# 193
result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)

# 194
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
    if (row[3] > 150):
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