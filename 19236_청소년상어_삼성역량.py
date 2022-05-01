
import sys
input = sys.stdin.readline

fish_num = []
fish_direction = []
fish_info = {}

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    li = list(map(int,input().split()))
    num_row = []
    direction_row = []
    for j in range(0,8,2):
        a, b = li[j], li[j+1]
        num_row.append(a)
        direction_row.append(b)
        fish_info[str(a)] = [i,j//2]
    fish_num.append(num_row)
    fish_direction.append(direction_row)

count = 0
count += fish_num[0][0]
fish_num[0][0] = 0
shark_direction = fish_direction[0][0]

print(fish_num)

def move_fish(num):
    y = fish_info[str(num)][0]
    x = fish_info[str(num)][1]
    ny = dy[fish_direction[y][x] - 1] + y
    nx = dx[fish_direction[y][x] - 1] + x
    
    if (0 <= ny < 4) and ( 0 <= nx < 4) and (fish_num[y][x] != 0) :
        fish_num[ny][nx] , fish_num[y][x] = fish_num[y][x] , fish_num[ny][nx]
    else :
        
    
print(fish_num)