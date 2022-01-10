import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(16)]

for i in range(1, N+1):
    day, price = input().split()
    day = int(day)
    price = int(price)
    if i + day - 1 <= N:
        dp[i + day - 1] = max(dp[i + day - 1], dp[i-1] + price)

    for j in range(i, min(i + day - 1, N)):
        dp[j] = max(dp[j], dp[i - 1])

num = 0
for i in range(16):
    num = max(num, dp[i])

print(num)

