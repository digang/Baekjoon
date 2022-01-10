import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [i for i in range(N+1)]
cost = list(map(int,input().split()))
cost.insert(0,int(0))

def find(x):
    if (x == arr[x]):
        return x
    else:
        y = find(arr[x])
        arr[x] = y
        return y

def union_insert(x,y):
    A = find(x)
    B = find(y)
    if A == B :
        return
    elif (cost[A] > cost[B]) :
        arr[A] = B
    else:
        arr[B] = A


for _ in range(M):
    a, b = map(int, input().split())
    union_insert(a,b)

mincost = int(0)

for i in range(1,N+1):
    mincost += cost[find(i)]
    cost[find(i)] = 0

print(mincost if mincost <= K else "Oh no")

