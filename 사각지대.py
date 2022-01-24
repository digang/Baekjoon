import sys
from collections import deque
from turtle import down
sys.stdin.readline
n,m = map(int,input().rsplit())

world = [list(map(int, input().rsplit())) for _ in range(n)]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def raiser(a,b,dirction):
    if dirction == UP:
        for i in range(a,-1,-1):
            if(world[i][b] == 6):
                break

            if(world[i][b] == 0):
                world[i][b] = 7
            else:
                continue
            
    elif dirction == DOWN:
        for i in range(a,n):
            if(world[i][b] == 6):
                break

            if(world[i][b] == 0):
                world[i][b] = 7
            else:
                continue

    elif dirction == RIGHT:
        for i in range(b,m):
            if(world[a][i] == 6):
                break

            if(world[a][i] == 0):
                world[a][i] = 7
            else:
                continue
    else:
        for i in range(b,-1,-1):
            if(world[a][i] == 6):
                break

            if(world[a][i] == 0):
                world[a][i] = 7
            else:
                continue

def raiserbfs(a,b,world):
    for i in range(a,n):
        for j in range(b,m):
            if (world[i][j]== 1):
                raiser(i,j+1,RIGHT)

            elif (world[i][j] == 2):
                raiser(i,j+1,RIGHT)
                raiser(i,j-1, LEFT)

            elif (world[i][j] == 3):
                raiser(i-1,j, UP)
                raiser(i,j+1,RIGHT)

            elif (world[i][j] == 4):
                raiser(i-1,j, UP)
                raiser(i,j+1,RIGHT)
                raiser(i,j-1, LEFT)

            elif (world[i][j] == 5):
                raiser(i-1,j, UP)
                raiser(i,j+1,RIGHT)
                raiser(i,j-1, LEFT)
                raiser(i+1,j,DOWN)

for i in range(n):
    for j in range(m):
        if (world[i][j]== 1):
            raiser(i,j+1,RIGHT)

        elif (world[i][j] == 2):
            raiser(i,j+1,RIGHT)
            raiser(i,j-1, LEFT)

        elif (world[i][j] == 3):
            raiser(i-1,j, UP)
            raiser(i,j+1,RIGHT)

        elif (world[i][j] == 4):
            raiser(i-1,j, UP)
            raiser(i,j+1,RIGHT)
            raiser(i,j-1, LEFT)

        elif (world[i][j] == 5):
            raiser(i-1,j, UP)
            raiser(i,j+1,RIGHT)
            raiser(i,j-1, LEFT)
            raiser(i+1,j,DOWN)

def bfs(a,b):
    count =0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((a,b))
    while q:
        y, x = q.popleft()
        count += 1
        visit[y][x] = 1
        up_y = y + 1 if y + 1 < n else y
        up_x = x + 1 if x + 1 < m else x
        down_y = y - 1 if y -1 >= 0 else y
        down_x = x - 1 if x -1 >= 0 else x
        if ( visit[up_y][x] == 0):
            q.append((up_y,x))
        elif (visit[down_y][x] == 0):
            q.append((down_y,x))
        elif (visit[y][down_x] == 0):
            q.append((y,down_x))
        elif (visit[y][up_x] == 0):
            q.append((y,up_x))
    
    return count

print(world)

count = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(world[i][j] == 7 and visited[i][j] == 0):
            visited[i][j] = 1
            count = min(count,bfs(i,j))

print(count)