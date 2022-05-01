import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

R, C, N = map(int,input().split())
board = [ list(input().strip()) for _ in range(R)] 

#폭탄 설치된 위치
booms = []

# booms = [(1.3) , (2,4) , (4,0), (5,1)]
boom_count = 3

for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            booms.append((i,j))

for _ in range(N):
    boom_count -= 1
    
    if boom_count == 1: 
        for i in range(R):
            # 0 ~ R
            for j in range(C):
                # 0 ~ C
                if board[i][j] == '.':
                    board[i][j] = 'O'
    
    if boom_count == 0:
        for boom in booms:
            y, x = boom
            board[y][x] = '.'
            for i in range(4):
                # y,x = 3,3
                ny = y + dy[i] # 2 4 3 3
                nx = x + dx[i] # 3 3 2 4
                
                if 0 <= ny < R and 0 <= nx < C:
                    board[ny][nx] = '.'

        booms = []
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    booms.append((i,j))
        
        boom_count = 2


for i in range(R):
    for j in range(C):
        print(board[i][j],end='')
    print()