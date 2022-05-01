import sys
from collections import deque
input = sys.stdin.readline

L = int(input())
N = int(input())

# 상 우 하 좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

change = deque()
for _ in range(N):
    t, dir = input().split()
    change.append((int(t),dir))

# 뱀의 머리는 오른쪽.
head = (L,L,1)
board = [ [0] * (2*L + 1) for _ in range(2*L + 1)]
board[L][L] = 1
time = 0

while True:
    dir = 0
    
    if change:
        t, dir = change.popleft()
        for i in range(t):
            sy, sx, snake_dir = head
            time += 1
            ny = sy + dy[snake_dir]
            nx = sx + dx[snake_dir]
            head = (ny,nx,snake_dir)
            if board[ny][nx] == 1 or not 0 <= ny < (2*L +1) or not 0<= nx < (2*L+1):
                print(time)
                sys.exit()
            board[ny][nx] = 1

    else:
        while True:
            sy, sx, snake_dir = head
            time += 1
            ny = sy + dy[snake_dir]
            nx = sx + dx[snake_dir]
            head = (ny,nx,snake_dir)
            if board[ny][nx] == 1 or not 0 <= ny < (2*L +1) or not 0<= nx < (2*L+1):
                print(time)
                sys.exit()
            board[ny][nx] = 1
            print(board)
        
    if dir == 'L':
        snake_dir = (snake_dir - 1 + 4) % 4
    elif dir == 'R':
        snake_dir = (snake_dir + 1 + 4) % 4
    
    y, x, d = head
    head = (y, x, snake_dir)
