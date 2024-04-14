n = int(input())

#모두 0으로 초기화
dp = [0] * 1001

# SK == 0, CY == 1
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4,n+1):
    dp[i] = (dp[i-1] + 1) % 2

print("SK" if dp[n] == 0 else "CY")