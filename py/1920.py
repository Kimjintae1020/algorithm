N = int(input())
li_N = set(map(int,input().split()))

M = int(input())
li_M = list(map(int,input().split()))

for num in li_M:
    print(1) if num in li_N else print(0)