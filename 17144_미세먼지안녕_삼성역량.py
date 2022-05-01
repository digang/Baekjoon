import sys
import copy

input = sys.stdin.readline

r, c, t = map(int,input().split())  

world = [list(map(int,input().split())) for _ in range(r)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

cleaner_row = 0
for i in range(r):
    if world[i][0] == -1:
        cleaner_row = i
        break

def dust(_world):
    nextworld = copy.deepcopy(_world)
    for i in range(r):
        for j in range(c):
            if _world[i][j] > 0:
                div = _world[i][j] // 5
                for k in range(4):
                    ny = i + dy[k] if 0 <= i + dy[k] < r else i
                    nx = j + dx[k] if 0 <= j + dx[k] < c else j
                    if ny != i or nx != j:
                        if world[ny][nx] == -1:
                            continue
                        
                        nextworld[ny][nx] += div
                        nextworld[i][j] -= div

    return nextworld

def cleaner(_world , direction):
    nextworld = copy.deepcopy(_world)
    row = cleaner_row
    column = 1
    if direction == 1:
        row = cleaner_row + 1
    
    while True:
        nextworld[row][column + 1] = _world[row][column]
        column += 1
        if column == c-1:
            break
    
    while True:
        nextworld[row + direction][column] = _world[row][column]
        row += direction
        if row == 0 or row == r-1:
            break
    
    while True:
        nextworld[row][column - 1] = _world[row][column]
        column -= 1
        if column == 0:
            break
    
    while True:
        nextworld[row - direction][column] = _world[row][column]
        row -= direction
        if row == cleaner_row - 1 or row == cleaner_row + 2:
            break
    
    if direction == 1:
        nextworld[cleaner_row + 1][1] = 0
    else:
        nextworld[cleaner_row][1] = 0
    
    
    return nextworld

while t > 0:
    world = dust(world)
    
    world = cleaner(world,-1)
    world = cleaner(world, 1)
    
    t -= 1

count = 0
for row in world:
    for item in row:
        count += item


print(count + 2)