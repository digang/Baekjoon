import sys
input = sys.stdin.readline

def set_space(positions):
    vote1, vote2, vote3, vote4, vote5 = 0,0,0,0,0
    space = [ [5] * N for _ in range(N)]
    
    # 구역 1
    x, y, d1, d2 = positions
    for j in range(x-1, -1, -1):
        for i in range(y-1, -1 ,-1):
            space[i][j] = 1
            
            
    for _ in range(d1 + 1):
        space[y][x] = 5
        for j in range(y-1, -1, -1):
            space[j][x] = 1
        y -= 1
        x += 1
    
    # 구역 3
    x, y, d1, d2 = positions
    for j in range(x-1, -1,-1):
        for i in range(y, N):
            space[i][j] = 3
            
    
    for _ in range(d2 + 1):
        space[y][x] = 5
        for j in range(y+1,N):
            space[j][x] = 3
            
        y += 1
        x += 1
    
    # 구역 2
    x, y, d1, d2 = positions
    for i in range(y - d1 - 1, -1, -1):
        for j in range( x + d1 +1,N):
            space[i][j] = 2
            

    for _ in range(d2+1):
        space[y - d1][x + d1] = 5
        for j in range(x + d1 +1,N):
            space[y-d1][j] = 2
            
        x += 1
        y += 1
    
    x, y, d1, d2 = positions
    for i in range(x+d2+d1 + 1,N):
        for j in range(y+d2-d1+1,N):
            space[j][i] = 4
            
    for _ in range(d1 + 1):
        space[y + d2][x + d2] = 5
        for j in range(y+d2+1,N):
            space[j][x + d2] = 4
            
        x += 1
        y -= 1
    
    for i in range(N):
        for j in range(N):
            if space[i][j] == 5:
                vote5 += A[i][j]
            elif space[i][j] == 4:
                vote4 += A[i][j]
            elif space[i][j] == 3:
                vote3 += A[i][j]
            elif space[i][j] == 2:
                vote2 += A[i][j]
            else :
                vote1 += A[i][j]
    
    
    
    max_value = max(vote1,vote2,vote3,vote4,vote5)
    min_value = min(vote1,vote2,vote3,vote4,vote5)
    
    return (max_value - min_value)

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

ans = 1e15

for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                if d1 >= 1 and d2 >= 1 and 0 <= x < x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:
                    ans = min(ans, set_space((x,y,d1,d2)))

print(ans)
