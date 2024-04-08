n = int(input())
m = int(input())

ans = []

term3 = m%10
num3 = n * term3
ans.append(num3)    # 2360

#  n * 8
term4 = ((m - term3) // 10) % 10         # term = 8
num4 = n * term4

ans.append(num4)    # 3776

term5 = ((m - term3) // 10) // 10               # 3

num5 = n * term5
ans.append(num5)    #1416

sum = num3 + (num4 * 10) + (num5 * 100)
ans.append(sum)

for element in ans:
    print(element)