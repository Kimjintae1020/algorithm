li = []

for _ in range(10):
    num = int(input())
    li.append(num%42)

a = set(li)
count = len(li) - len(a)
print(len(a))
