import sys
from collections import deque
import copy
input = sys.stdin.readline

N, K, R = map(int,input().split())
farm = [ [[] for _ in range(N)] for _ in range(N) ]
visited = [ [False] * N for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

cows = [ [0] * N for _ in range(N)]

count = 0

for _ in range(R):
    r1, c1, r2, c2 = map(int,input().split())
    farm[r1 - 1][c1 - 1].append([r2 -1, c2-1])
    farm[r2 - 1][c2 - 1].append([r1 - 1, c1 - 1])

for _ in range(K):
    r, c = map(int,input().split())
    cows[r-1][c-1] = 1

def bfs(position, visit, cowmap):
    q = deque()
    q.append(position)
    
    while q:
        r, c = q.popleft()
        if visit[r][c]:
            continue
        
        else:
            visit[r][c] = 1
            cowmap[r][c] = 0
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                position = (nr,nc)
                po_list = [nr,nc]
                roads = farm[r][c]
                
                if po_list in roads:
                    continue
                
                if 0 <= nr < N and 0 <= nc < N:
                    q.append(position)
    return cowmap

for i in range(N):
    for j in range(N):
        if cows[i][j]:
            cowmap = bfs((i,j), copy.deepcopy(visited),copy.deepcopy(cows))
        else : continue
        
        for k in range(N):
            for z in range(N):
                if cowmap[k][z]:
                    count += 1

print(count // 2)
