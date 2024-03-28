a, x = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(a):
    if x > arr[i]:
        print(arr[i], end=" ")
           