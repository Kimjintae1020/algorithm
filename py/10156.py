#10156

price, n, money = map(int,input().split())

#현재 가격 * 개수
num = price * n 

result = num - money
if result > 0:
    print(num - money)
else:
    print(0)

