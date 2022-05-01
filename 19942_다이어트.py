import sys
input = sys.stdin.readline

#단백질, 지방, 탄수화물, 비타민, 가격

N = int(input())
mins = list(map(int,input().split()))
infos = []
answer = []
global mincost
mincost = 1e16

for _ in range(N):
    infos.append(list(map(int,input().split())))

def isright(li):
    p, f, s, v = 0,0,0,0
    for i in li:
        a,b,c,d,e = infos[i]
        p += a
        f += b
        s += c
        v += d
    if p >= mins[0] and f >= mins[1] and s >= mins[2] and v >= mins[3]:
        return True
    
    return False

def cal_cost(li):
    cost = 0
    for i in li:
        cost += infos[i][-1]
    
    return cost

def dfs(li):
    global mincost
    if isright(li):
        cost = cal_cost(li)
        if mincost > cost:
            mincost = cost
            answer.append((cost,li))
            return True
        else: return

    for i in range(li[-1]+1, N):
        tmp = li.copy()
        tmp.append(i)
        sign = dfs(tmp)
        if sign : continue
        else:
            tmp.pop()

for i in range(N):
    dfs([i])

if answer:
    print(answer[-1][0])
    l = [ i+1 for i in answer[-1][1]]
    print(*l)
else:
    print(-1)