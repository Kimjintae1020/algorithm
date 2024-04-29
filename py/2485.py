n = int(input())

num_li = []
gaps = []

a = int(input())


# 가로수 배열을 구하기 위한 최대공약수 구하기 -> 그 차이를 먼저 담음
for i in range(n-1):
    num = int(input())
    gaps = gaps.append(num - a)
    a = num

print(num_li)
