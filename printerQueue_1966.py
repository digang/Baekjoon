import sys
from collections import deque
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    q = deque()
    heap = []
    count = 0

    priory = list(map(int, input().split()))
    for i in range(N):
        if i  == M:
            q.append([priory[i], True])
            heapq.heappush(heap, -1 * priory[i])
        else:
            q.append([priory[i], False])
            heapq.heappush(heap, -1 * priory[i])


    while 1:
        top = -1 * heap[0]
        now = q.popleft()

        if top == now[0]:
            count += 1
            heapq.heappop(heap)
            if now[1] == True:
                break
        else:
            q.append(now)

    print(count)



