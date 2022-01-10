import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    input_data = sys.stdin.readline().rstrip()
    graph[i] = [int(j) for j in input_data]

for j in range(M):
    for i in range(1,N):
        if graph[i][j] == 1:
            graph[i][j] = graph[i-1][j] + 1

max_size = 0
for i in range(N):
    arr = graph[i]
    arr.sort(reverse=True)
    for idx in range(len(arr)):
        size = (idx+1) * arr[idx]
        max_size = size if size > max_size else max_size

print(max_size)