arr = []
sum = 0

for i in range(5):
    a = int(input())
    sum = sum + a
    arr.append(a)

arr.sort()

print(sum // 5)
print(arr[2])
