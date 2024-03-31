from math import gcd

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))

#  gcd 못 쓰게 되어있음...