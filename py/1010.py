#1010

def fac(n):
    term = 1
    for i in range(1, n+1):
        term *= i
    return term

n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    num = fac(b) // (fac(a) * fac(b-a))
    print(num)
