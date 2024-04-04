n, k = map(int,input().split())

arr = []
count = 0

for _ in range(n):
    arr.append(int(input()))

    
for i in reversed(range(n)):
    count+= k // arr[i]
    k = k % arr[i]

print(count)