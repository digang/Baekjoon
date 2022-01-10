import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
world = [[0 for _ in range(M)] for _ in range(N)]

def findpath(n, m):
    hour = [[100001 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([n,m,int(0)])
    count = int(-1)
    hour[n][m] = 0

    while q:
        info = q.popleft()

        n_up = info[0] + 1
        if n_up == N:
            n_up -= 1
        n_down = info[0] - 1
        if n_down == -1:
            n_down = 0
        m_up = info[1] + 1
        if m_up == M:
            m_up -= 1
        m_down = info[1] - 1
        if m_down == -1:
            m_down += 1


        if (count < info[2]):
            count = info[2]

        # 0, 3
        if world[info[0]][m_up] == 'L' and hour[info[0]][m_up] > info[2] + 1:
            hour[info[0]][m_up] = info[2] + 1
            q.append([info[0],m_up,info[2] + 1])

        # 0, 1
        if world[info[0]][m_down] == 'L' and hour[info[0]][m_down] > info[2] + 1:
            hour[info[0]][m_down] = info[2] + 1
            q.append([info[0],m_down,info[2] + 1])
        # 1, 2
        # print(str(n_up) + " " + str(m))
        # print(world[n_up][m])
        # print(hour[n_up][m])
        # print(info[2] + 1)
        if world[n_up][info[1]] == 'L' and (hour[n_up][info[1]] > info[2] + 1):
            hour[n_up][info[1]] = info[2] + 1
            q.append([n_up,info[1],info[2] + 1])
        # 0, 2
        if world[n_down][info[1]] == 'L' and hour[n_down][info[1]] > info[2] + 1:
            hour[n_down][info[1]] = info[2] + 1
            q.append([n_down,info[1],info[2] + 1])

    return count

for i in range(N):
    line = input()
    for j in range(M):
        world[i][j] = line[j]

cnt = 0
for i in range(N):
    for j in range(M):
        if world[i][j] == 'L':
            path = findpath(i,j)
            if cnt < path:
                cnt = path

print(str(cnt))
