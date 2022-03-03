import sys
import copy
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [ [False] * c for _ in range(r)]
    visited[y][x] = True
    cluster = []
    cluster.append((y,x))
    flag = False
    
    while q:
        a, b = q.pop()
        if b == r - 1 :
            flag = True
        
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < r and 0 <= nx < c and cave[ny][nx]=='x':
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                q.append((ny,nx))
                cluster.append((ny,nx))
    
    return cluster, flag

def fall(cluster):
    cnt = 0
    for item in cluster:
        y, x = item
        cave[y][x] = '.'
    flag = False
    
    copy_cluster = copy.deepcopy(cluster)
    
    while True:
        for idx,item in enumerate(copy_cluster):
            y, x = item
            if 0 <= y+1 < r and cave[y+1][x] != 'x':
                copy_cluster[idx] = (y+1,x)
            else:
                flag = True
        if flag:
            break
        cnt += 1
    
    for item in cluster:
        y, x = item
        cave[y+cnt][x] = 'x'

def crush(position):
    y, x = position
    cave[y][x] = '.'
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and cave[ny][nx]=='x':
            cluster , flag = bfs(ny,nx)
            if cluster:
                if flag:
                    continue
                fall(cluster)

# 동굴 
cave = [ list(input().strip()) for _ in range(r)]
n = int(input())

# 던지는 높이
throw = list(map(int,input().split()))

for i in range(n):
    height = throw[i]
    
    if i % 2 == 0:
        for j in range(c):
            if cave[r - height][j] == 'x':
                crush( (r- height, j))
                break
    elif i % 2 == 1:
        for j in range(c):
            if cave[r - height][-j -1 ] == 'x':
                crush( ( r - height, c - j - 1))
                break

for i in range(r):
    for j in range(c):
        print(cave[i][j], end='')
    print()