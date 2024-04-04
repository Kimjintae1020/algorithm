n = int(input())

li = []
total = 0

for _ in range(n):
    num = int(input())

    if num == 0:
        if li:
            remove_num = li.pop()
            total -= remove_num

    else:
        li.append(num)
        total += num

print(total)

