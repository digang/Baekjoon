import sys
import math
input = sys.stdin.readline


# 동 북 서 남
dx = [1,0,-1,0]
dy = [0,-1,0,1]

world= [[0 for _ in range(101)] for _ in range(101)]

n = int(input())
for i in range(n):
    x, y, d, g = map(int, input().split())  
    world[y][x] = 1
    move = [d]
    for i in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-1-i] + 1) % 4)
        move.extend(temp)
    for i in move:
        nx = dx[i] + x
        ny = dy[i] + y
        world[ny][nx] = 1
        x = nx
        y = ny

count = 0
for i in range(100):
    for j in range(100):
        if world[i][j] and world[i][j + 1] and world[i + 1][j] and world[i + 1][j + 1]:
            count += 1

print(count)