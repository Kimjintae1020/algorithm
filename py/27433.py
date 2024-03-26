n = int(input())

if n == 0:
    print(1)

else:
    answer = 1
    for i in range(2,n+1):
        answer = answer * i
    print(answer)