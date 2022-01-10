import sys
import copy
from collections import deque
input = sys.stdin.readline

def MoveEast(copydice):
    EAST = copydice[2]
    SOUTH = copydice[1]
    NORTH = copydice[3]
    WEST = copydice[4]
    TOP = copydice[0]
    UPPER = copydice[5]

    copydice[0] = WEST
    copydice[1] = SOUTH
    copydice[2] = TOP
    copydice[3] = NORTH
    copydice[4] = UPPER
    copydice[5] = EAST

    return copydice

def MoveNorth(copydice):
    EAST = copydice[2]
    SOUTH = copydice[1]
    NORTH = copydice[3]
    WEST = copydice[4]
    TOP = copydice[0]
    UPPER = copydice[5]

    copydice[0] = SOUTH
    copydice[1] = UPPER
    copydice[2] = EAST
    copydice[3] = TOP
    copydice[4] = WEST
    copydice[5] = NORTH

    return copydice

def MoveWest(copydice):
    EAST = copydice[2]
    SOUTH = copydice[1]
    NORTH = copydice[3]
    WEST = copydice[4]
    TOP = copydice[0]
    UPPER = copydice[5]

    copydice[0] = EAST
    copydice[1] = SOUTH
    copydice[2] = UPPER
    copydice[3] = NORTH
    copydice[4] = TOP
    copydice[5] = WEST

    return copydice

def MoveSouth(copydice):
    EAST = copydice[2]
    SOUTH = copydice[1]
    NORTH = copydice[3]
    WEST = copydice[4]
    TOP = copydice[0]
    UPPER = copydice[5]

    copydice[0] = NORTH
    copydice[1] = TOP
    copydice[2] = EAST
    copydice[3] = UPPER
    copydice[4] = WEST
    copydice[5] = SOUTH

    return copydice

dice = [0 for _ in range(6)]
n, m, y, x, k = map(int,input().split())
positiony = y
positionx = x
dy = [-1,1,0,0]
dx = [0,0,-1,1]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

q = deque()
li = list(map(int,input().split()))
for item in li:
    q.append(item)

def start(py,px):
    y = py
    x = px
    global dice
    while q:
        flag = False
        direction = q.popleft()
        if direction == 1: #east
            if (x+1) < m:
                flag = True
                x += 1
                dice = MoveEast(copy.deepcopy(dice))
                if graph[y][x] == 0:
                    graph[y][x] =dice[5]
                else :
                    dice[5] = graph[y][x]
                    graph[y][x] = 0
        elif direction == 2: #west
            if (x-1) >= 0:
                flag = True
                x -= 1
                dice = MoveWest(copy.deepcopy(dice))
                if graph[y][x] == 0:
                    graph[y][x] = dice[5]
                else:
                    dice[5] = graph[y][x]
                    graph[y][x] = 0
        elif direction == 3: #north
            if (y -1) >= 0:
                flag = True
                y-=1
                dice = MoveNorth(copy.deepcopy(dice))
                if graph[y][x] == 0:
                    graph[y][x] = dice[5]
                else:
                    dice[5] = graph[y][x]
                    graph[y][x] = 0
        else:
            if(y+1) < n:
                y+=1
                flag = True
                dice = MoveSouth(copy.deepcopy(dice))
                if graph[y][x] == 0:
                    graph[y][x] = dice[5]
                else:
                    dice[5] = graph[y][x]
                    graph[y][x] = 0

        if flag == True :
            print(dice[0])

start(positiony,positionx)