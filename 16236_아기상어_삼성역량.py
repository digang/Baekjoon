from os import minor
from re import X
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
world = [list(map(int,input().split())) for _ in range(n)]
shark_y = 0
shark_x = 0
shark_size = 2
size_count = 0
time = 0

# 북 동 남 서
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        if world[i][j] == 9:
            shark_y = i
            shark_x = j

def find_fish(y,x):
    visited = [ [0] * n for _ in range(n)]
    q = deque()
    info = {'y' : y , 'x' : x, 'distance' : 0}
    q.append(info)
    
    min_y = 22
    min_x = 22
    mindistance = 9999999
    while q:
        
        _info = q.popleft()
        y = _info['y']
        x = _info['x']
        distance = _info['distance']
        
        if visited[y][x] == 1:
            continue
        
        visited[y][x] = 1
        if world[y][x] != 0 and world[y][x] != 9 and world[y][x] <= shark_size:
            if world[y][x] < shark_size:
                if distance <= mindistance:
                    mindistance = distance
                    if min_y >= y:
                        min_y = y
                        min_x = min(min_x,x)
                else:
                    continue
            
        elif world[y][x] != 0 and world[y][x] != 9 and world[y][x] > shark_size:
            continue
        
        for i in range(4):
            ny = y + dy[i] if 0 <= y + dy[i] < n else y
            nx = x + dx[i] if 0 <= x + dx[i] < n else x
            if visited[ny][nx] == 0:
                new_info = {'y' : ny , 'x': nx , 'distance': distance + 1}
                q.append(new_info)
                
    return (min_y,min_x,mindistance)

    
while True:    
    miny, minx, mindistance = find_fish(shark_y,shark_x)
    if minx != 22:
        size_count += 1
        if shark_size == size_count:
            shark_size += 1
            size_count = 0
        world[shark_y][shark_x] = 0
        shark_y = miny
        shark_x = minx
        world[shark_y][shark_x] = 9
        time += mindistance
        
    
    else:
        print(time)
        break