import sys
input = sys.stdin.readline
INF = sys.maxsize

SIZE = int(input())
board = [list(map(int,input().split())) for _ in range(SIZE)]
dp = [[0] * SIZE for _ in range(SIZE)]
dp[0][0] = 1

for i in range(SIZE):
    for j in range(SIZE):
        if i == SIZE - 1 and j == SIZE - 1:
            print(dp[i][j])
            break
        cur_cnt = board[i][j]

        if j + cur_cnt < SIZE :
            dp[i][j+cur_cnt] += dp[i][j]

        if i + cur_cnt < SIZE :
            dp[i+cur_cnt][j] += dp[i][j]


