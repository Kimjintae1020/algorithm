a, b, c = map(int, input().split())

term = a
for i in range(b-1):
    term = term * a

print(term % c)

## 시간초과...강해져서 돌아오기..