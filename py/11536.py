n = int(input())

arr = []

for _ in range(n):
    name = input()
    arr.append(name)


# 오름차순
if sorted(arr) == arr:
    print("INCREASING")

# 내림차순 
elif sorted(arr, reverse=True) == arr:
    print("DECREASING")
    
else:
    print("NEITHER")
    