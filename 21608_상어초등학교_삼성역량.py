import sys
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def check(y,x,info):
    cnt = 0
    vacant_cnt = 0
    num, a,b,c,d = info
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if not classroom[ny][nx]:
                vacant_cnt += 1
            if classroom[ny][nx] == a or classroom[ny][nx] == b or classroom[ny][nx] == c or classroom[ny][nx] == d:
                cnt += 1
    return cnt, vacant_cnt

def find_seat(info):
    max_count = -1
    vacant_count = -1
    r,c = 0,0
    
    for i in range(N):
        for j in range(N):
            if not classroom[i][j]:
                cnt, vacant_cnt = check(i,j,info)
                
                if cnt > max_count:
                    max_count = cnt
                    vacant_count = vacant_cnt
                    r,c = i,j
                    continue
                
                if cnt == max_count:
                    if vacant_cnt > vacant_count:
                        vacant_count = vacant_cnt
                        r,c = i,j
                    continue
    return r,c

N = int(input())
likes = [0] * (N*N)
classroom = [ [0] * N for _ in range(N)]
counts = [ [0] * N for _ in range(N)]

for i in range(N*N):
    s_num, a, b, c, d = map(int,input().split())
    likes[i] = (s_num,a,b,c,d)

for info in likes:
    r,c = find_seat(info)
    classroom[r][c] = info[0]
    counts[r][c] = [ item for item in info[1:]]

result = 0

for i in range(N):
    for j in range(N):
        count = 0 
        a,b,c,d = counts[i][j]
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0<= ny < N and 0 <= nx < N:
                if classroom[ny][nx] == a or classroom[ny][nx] == b or classroom[ny][nx] == c or classroom[ny][nx] == d: 
                    count += 1
        
        if count > 0:
            result += 10 ** (count - 1)
print(result)