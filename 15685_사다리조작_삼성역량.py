import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())
line = [ [0] * (N+1) for _ in range(H+1)]
for _ in range(1,M+1):
    a, b = map(int,input().split())
    line[a][b] = 1

def check():
    for start in range(1,N+1):
        k = start
        for j in range(H+1):
            if line[j][k]:
                k += 1
            elif k > 1 and line[j][k-1]:
                k -= 1
        if k != start: return False
    
    return True

def dfs(cnt, x, y):
    # x = row
    # y = col
    global ans
    
    if check():
        ans = min(ans, cnt)
        return 
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(x, H):
        if i == x: k = y
        else : k = 0
        for j in range(k, N):
            if not line[i][j] and not line[i][j+1]:
                if j > 1 and line[i][j-1] : continue
                
                line[i][j] = 1
                dfs(cnt +1, i, j + 2)
                line[i][j] = 0
                
ans = 4
dfs(0,0,0)
print( ans if ans <4 else -1)