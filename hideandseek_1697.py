import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int,input().split())
visited = [False for _ in range(100001)]

def BFS(now):
    count = 0
    q = deque([[now,count]])
    while q :
        v = q.popleft()
        e = v[0]
        count = v[1]

        if not visited[e]:
            visited[e] = True
            if e == K:
                return count

            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])

            if (e + 1) <= 100000:
                q.append([e + 1, count])

            if (e - 1) >= 0:
                q.append([e - 1, count])

    return count

print(BFS(N))


