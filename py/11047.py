n, k = map(int,input().split())

arr = []
count = 0

for _ in range(n):
    num = int(input())
    arr.append(num)

# 내림차순으로 정렬
arr.sort(reverse=True)

k