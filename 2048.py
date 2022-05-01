import sys
input = sys.stdin.readline

def move(direction):
    a = 3
    # do something

left = []
up = []
right = []
down = []

dict ={0: left, 1 : up, 2 : right, 3: down}

N = int(input().split())
board = [list(map(int,input().split()))]

cnt = 0
ans = 0
for k in range(5):
    for i in range(4):
        if cnt == 5:
            print(ans)
            sys.exit()

        direction = dict[i]
        move(direction)
        
        cnt += 1