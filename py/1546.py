x = int(input())
term = list(map(int, input().split()))

max_term = max(term)

for i in range(x):
    term[i] = term[i]/max_term * 100

print(sum(term) / x)
