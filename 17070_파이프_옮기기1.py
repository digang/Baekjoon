import sys
from collections import deque
input = sys.stdin.readline

RIGHT_STRAIGHT = 0
DIAGONAL_STRAIGHT = 1
DOWN_STRAIGHT = 2

def check(y,x,d):
    for direction in directions[d]:
        dy, dx = cos[direction]
        ny = y + dy
        nx = x + dx
        if ny < N and nx < N and not m[ny][nx]:
            if direction != 1:
                count[ny][nx][direction] += count[y][x][d]
            else:
                if not m[ny - 1][nx] and not m[ny][nx - 1]:
                    count[ny][nx][direction] += count[y][x][d]

N = int(input())
m = [ list(map(int,input().split())) for _ in range(N)]
count = [ [ [0] * 3 for _ in range(N) ] for _ in range(N)]

# 0 : 오른쪽 1 : 대각선 2: 아래
directions = { 0 : [0,1] , 1 : [0,1,2] , 2: [1,2]}
cos = {0 : [0,1] , 1 : [1,1] , 2: [1,0]}

count[0][1][0] = 1

for i in range(N):
    for j in range(N):
        for d in range(3):
            if count[i][j][d] and not m[i][j]:
                check(i,j,d)

print(sum(count[N-1][N-1]))