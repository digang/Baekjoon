import sys
input = sys.stdin.readline

def move(sy,sx,dir):
    global sand
    total = 0
    
    if sy < 0:
        return
    
    for y,x,z in dir:
        ny = sy + y
        nx = sx + x
        if z == 0 :
            new_sand = board[sy][sx] - total
        else:
            new_sand = int(board[sy][sx] * z)
            total += new_sand
        
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] += new_sand
        else:
            sand += new_sand
    board[sy][sx] = 0

N = int(input())
board = [list(map(int,input().split())) for _ in range(N) ]

left = [(1,-1,0.1), (-1,-1,0.1), (1,0,0.07), (-1,0,0.07), (2,0,0.02), (-2,0,0.02), (1,1,0.01) , (-1,1,0.01), (0,-2,0.05), (0,-1,0)]
right = [ (y, -x,z) for y,x,z in left]
up = [(x,y,z) for y,x,z in left]
down = [(-x,y,z) for y,x,z in left]

s_y , s_x = N//2 , N//2
sand = 0
# 좌 하 우 상
dy = [0,1,0,-1]
dx = [-1,0,1,0]

dict = { 0: left, 1: down, 2: right, 3 : up}
time = 0
for i in range(2*N -1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        n_y = s_y + dy[d]
        n_x = s_x + dx[d]
        move(n_y,n_x,dict[d])
        s_y, s_x = n_y, n_x

print(sand)
