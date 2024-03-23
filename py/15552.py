import sys

x = int(input())

for i in range(x):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
