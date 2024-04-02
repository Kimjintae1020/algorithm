total = int(input())
n = int(input())

sum = 0 

for _ in range(n):
    price, num = map(int,input().split())

    sum = sum + (price * num)

if total == sum:
    print("Yes")
elif total != sum:
    print("No")