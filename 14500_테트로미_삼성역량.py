import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

maxValue = 0


def dfs(y, x, dsum, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, dsum + graph[ny][nx], cnt+1)
            visited[ny][nx] = False

def exec(y, x):
    global maxValue
    for z in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = graph[y][x]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            t = (z + k) % 4
            ny = y + dy[t]
            nx = x + dx[t]
            if not (0 <= ny < n and 0 <= nx < m):
                tmp = 0
                break
            tmp += graph[ny][nx]
        # 최대값 계산
        maxValue = max(maxValue, tmp)




for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False
        exec(i, j)

print(maxValue)