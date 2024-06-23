n = int(input("Enter a number: "))

ans = 'int'

for i in range(n//4):
    ans = 'long ' + ans

print(ans)