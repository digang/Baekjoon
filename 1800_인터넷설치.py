import sys
import heapq
input = sys.stdin.readline

N, P, K = map(int,input().split())
INF = 1e15
graph = [[] for _ in range(N+1)]
for _ in range(P):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

left, right = 0, 1000001
answer = INF

def dijkstra(start, limit):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        cost, index = heapq.heappop(q)
        if distance[index] < cost:
            continue
        for item in graph[index]:
            if item[1] > limit:
                if cost + 1 < distance[item[0]]:
                    distance[item[0]] = cost + 1
                    heapq.heappush(q, (cost + 1, item[0]))
            else :
                if cost < distance[item[0]]:
                    distance[item[0]] = cost
                    heapq.heappush(q, (cost , item[0]))
                    
    if distance[N] > K:
        return False
    else:
        return True

while left<= right:
    mid = (left + right) // 2
    flag = dijkstra(1, mid)
    if flag:
        right = mid -1
        answer = mid
    else :
        left = mid + 1
        
if answer == INF:
    print(-1)
else :
    print(answer)
