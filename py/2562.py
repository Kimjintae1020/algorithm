
num = []

for _ in range(9):
    m = int(input())
    num.append(m)

max = max(num)
result = num.index(max) + 1
print(max)
print(result)