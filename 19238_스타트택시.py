import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def djaikstra(board,cost,client,now):
    y,x = now
    ny,nx = client
    if board[y][x] < cost:
        return
    else:
        board[y][x] = cost

    if now==client:
        return cost, client
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            cost , client = djaikstra(board,cost + 1, client, (ny,nx))





N, M, oil = map(int,input().split())
m = [ list(map(int,input().split())) for _ in range(N)]
a,b = map(int,input().split())
taxi = [a-1,b-1]
passengers =[]
for _ in range(M):
    a1, b1, a2, b2 = map(int,input().split())
    passengers.append([a1-1,b2-1,a2-1,b2-1])

while oil > 0:
