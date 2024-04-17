str = input()

cnt = 0

for i in range(len(str)-1):
    if str[i] == ' ':
        cnt += 1
    
if str[0] == ' ':
    cnt -= 1

print(cnt+1)
