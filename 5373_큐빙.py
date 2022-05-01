import sys
input = sys.stdin.readline

def spin(space, direction):
    global cube, up, down, left, right, front, back
    if space == 'U':
        space = up
    elif space == 'D':
        space = down
    elif space == "F":
        space = front
    elif space == 'B':
        space = back
    elif space == 'L':
        space = left
    else:
        space = right
    
    

T = int(input())    
while T>0:
    # 0 : white 윗면 , 1 : yellow 아랫면 , 2 : red 앞면, 3 : orange 뒷면, 4 : green 왼쪽, 5 : blue 오른쪽
    cube = [[ [i,i,i] for _ in range(3) ] for i in range(6)]
    up = [3,5,1,4]
    down = [2,5,3,4]
    left = [0,2,1,3]
    right = [2,0,3,1]
    front = [0,5,1,4]
    back = [0,4,1,5]
    
    n = int(input())
    a = input().split()
    for item in a:
        space = item[0]
        direction = item[1]
        spin(space,direction)
    T -= 1