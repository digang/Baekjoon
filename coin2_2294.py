import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [10001 for _ in range(k+1)]
dp[0] = 0

for _ in range(n):
    num = int(input())
    #print("num is %d" %num)
    for j in range(num, k+1):
        dp[j] = min(dp[j], dp[j - num] + 1)

if dp[k] != 10001:
    print(dp[k])
else:
    print("-1")



